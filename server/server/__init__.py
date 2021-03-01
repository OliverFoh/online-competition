# -*- coding: utf-8 -*-
import os,base64,uuid
from flask import Flask,render_template,request,session
from .controller.session_auth import login_required
from flask_uploads import UploadSet,configure_uploads,patch_request_class,IMAGES
import configparser
from server.models.user import mydb
from server.controller.sign_in import UserLogin
from flask_restful import Api
from flask_socketio import SocketIO,send,emit,join_room,leave_room,close_room
from datetime import timedelta,datetime
from threading import Lock
from engineio.payload import Payload

import threading
from server.controller.match.player_match import Player
import time
from queue import Queue
from server.controller.match.robot_match import Roboter
from server.controller.match.elo import PlayerScore
from .api import Login,Register,Password,LoginOut,PersonalInfo,RobotMatch,PlayerMatch,PersonAvatar,Rank

app = Flask(__name__,template_folder='./view/templates/',static_folder='./view/static')
"""初始化websocket配置"""
async_mode=None
Payload.max_decode_packets = 50
socketio = SocketIO(app,cors_allowed_origins='*',async_mode=async_mode)

""""""""""""""""""""""""



@app.route('/', methods=['get', 'post'])
def index():
    return render_template('upload.html')


def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = request.headers.get('Origin')
    response.headers['Access-Control-Allow-Credentials']='true'
    response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response

def create_app():

    api=Api(app)
    # app.config.from_pyfile('setting.py')
    # 数据库配置
    my_config = configparser.ConfigParser()
    my_config.read(os.path.dirname(__file__)+'/db.conf')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + my_config.get('DB', 'USER') + ':' + my_config.get('DB','PASSWORD') + '@' + my_config.get('DB', 'HOST') + '/' + my_config.get('DB', 'DB_NAME')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    #app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))

    # app.add_url_rule('/login',view_func=UserLogin.as_view('login'))
    mydb.init_app(app)

    #socketio.init_app(app)

    """session设置"""
    app.config['SECRET_KEY'] =os.urandom(24)
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)

    """""""""""""添加接口映射"""""""""""""

    #登录接口
    api.add_resource(Login,'/api/login')

    #退出登录接口
    api.add_resource(LoginOut, '/api/out')

    #注册接口
    api.add_resource(Register, '/api/register')

    #找回密码
    api.add_resource(Password, '/api/forgetPassword')

    #个人信息
    api.add_resource(PersonalInfo,'/api/user/viewPersonInfo','/api/user/modifyPersonInfo')

    #修改个人信息
    #api.add_resource(PersonalInfo,'/api/modifyPersonInfo')

    #修改用户头像
    api.add_resource(PersonAvatar, '/api/user/modifyPersonAvatar')

    #机器人模式接口
    api.add_resource(RobotMatch, '/api/robot')

    # 玩家匹配接口
    api.add_resource(PlayerMatch, '/api/player')

    #查看排行榜接口
    api.add_resource(Rank,'/api/rank/orderBy')

    """"""""""""""""""""""""""""""""""""""






    """设置跨域请求权限"""
    app.after_request(after_request)
    return app

""""""""""""""""""""
# 全局玩家匹配等待池
player_pool = Player()

#全局匹配成功池
player_double_pool=[]

""""""""""""""""""""




thread = None
thread_lock = Lock()



# def threadTest():
#     print('后台匹配线程启动')
#     while True:
#         if player_pool.printQueueNum() == 2:
#             print('匹配成功')
#             # 创建房间
#             room = str(uuid.uuid1())
#             player_list = []
#             player_list.append(player_pool.popPlayer())
#             player_list.append(player_pool.popPlayer())
#             print('当前用户%s 与 用户%s匹配成功', player_list[0], player_list[1])
#             print(player_pool.printQueueNum())
#             print(player_list)
#
#             #记录在全局匹配池
#             player_double_pool.put(player_list)
#             #join_room(room=room)
#             # 抽取试题
#             # question_list = player_pool.getQuestionList()
#             # print(question_list)
#
#             # 给客户端回执
#             socketio.emit('server_response',
#                           {'match': True, 'connect': True, 'ready':False,'data': player_list,'msg':'返回玩家信息'}, namespace='/compete')
#
#
#             socketio.start_background_task(background_thread)
#             return {'data': '即将发送试题'}
#

# thread=threading.Thread(name='compete',target=threadTest)
# thread.setDaemon(True)
# thread.start()

#socketio.start_background_task(target=threadTest())

# @app.route('/')
# def index():
#     return render_template('index.html')

@socketio.on('connect', namespace='/compete')
@login_required
def test_connect():
    print('%s成功连接websocket' %session.get('account'))
    #print(request.headers)
    emit('connect',{'match':False,'connect':True,'ready':False,'msg':'连接成功'},namespace='/compete')      #返回连接成功状态

@login_required
@socketio.on('join',namespace='/compete')
def on_join(data):
    print(data)
    if 'account' in session:
        #print('该账号已经登录')
        username=session.get('account')
        print('%s正在匹配中...' %username)
        #print(username)
        player_pool.pushPlayer(id='2')
        player_pool.pushPlayer(username)
    print('当前在线用户数为 %s'% player_pool.printQueueNum())
    if player_pool.printQueueNum() >= 2:
        print('匹配成功')
        # 创建房间
        room = str(uuid.uuid1())
        player_list = []
        player_list.append(player_pool.popPlayer())
        player_list.append(player_pool.popPlayer())
        for item in player_list:
            item['current_score']=0
            item['current_index']=0
            item['rescueRate']=0
            item['structureRate']=0
            item['predictRate']=0
            item['correctNum']=0
            item['score']=0
            item['is_answer']=None
            item['is_end']=False
            item['is_win']=False
            item['last_isFinish']=False
        pk_player=player_list[0]

        # 抽取试题
        question_list = player_pool.getQuestionList()
        print(question_list)
        player_list.append(question_list)
        #player_list中前两个元素为玩家信息，最后一个为分配到的题目列表
        player_double_pool.append(player_list)

        print('当前用户%s 与 用户%s匹配成功', player_list[0], player_list[1])
        print(player_pool.printQueueNum())
        print(player_list)
        # join_room(room=room)


        # 给客户端回执
        socketio.emit('server_response',
                      {'match': True, 'connect': True, 'type':'playerInfo','ready': False, 'data': pk_player, 'msg': '返回玩家信息'},
                      namespace='/compete')
        socketio.start_background_task(background_thread,player_double_pool)
        return {'data': '匹配成功,即将发送试题'}
    return '人数不够，待会来试吧'



#发送试题方法
def sendQuestions(question):
    #socketio.start_background_task(background_thread,question_list)
    socketio.emit('server_response',
                  {'match': True, 'connect': True, 'type': 'question', 'ready': True, 'data': question},
                  namespace='/compete', broadcast=True)


#接收每道题得分
@socketio.on('scoreInfo',namespace='/compete')
def handle_scoreInfo(data):
    print(data)
    if data['is_end']==True:
        handle_final(data)
        return '游戏结束,返回最终结果'
    user_id=session.get('account')
    current_score = data['current_score']
    for item in player_double_pool:
        for player in item:
            if 'account' in player:
                if player['account']==user_id:
                    player['current_score']=current_score
                    player['score']=player['score']+current_score
                    player['is_answer']=data['is_answer']
                    player['current_index']=data['currentQuestionIndex']
                    break
    #十道题全部发放完毕
    # if data['is_end']==True:
    #
    #     print()
    socketio.emit('server_response',
                  {'match': True, 'connect': True, 'type': 'scoreInfo', 'ready': True, 'data': {'id':user_id,'current_score':current_score},
                   'msg': '返回对方成绩'},
                  namespace='/compete',broadcast=True)


    for item in player_double_pool:
        # 发送下一道题,共有以下两种情况
        #1.两个人有任一方超时未作答，则直接切换下一题
        #2.两个人当前题目序号一致，即两个人都在规定时间作答

        #两人都在规定时间内作答完毕提前推送试题
        if item[0]['is_answer']==True and item[1]['is_answer']==True:
            print('发送题目啦')
            print(item[2][data['currentQuestionIndex']])
            sendQuestions(question=item[2][data['currentQuestionIndex']])


    print('该题得分为%s' %current_score)
    return '分数上传成功'

def handle_final(data):
# 用时
# 最后分数
    player=player_double_pool[0]
    if player[0]['score']>player[1]['score']:   #玩家1胜利
        player[0]['is_win']=True
        socketio.emit('server_response',
                      {'match': True, 'connect': True, 'type': 'finalResult', 'ready': True, 'winer': {'id':player[0]['account'],'nick_name':player[0]['account'],'score':player[0]['score']}},
                      namespace='/compete', broadcast=True)
    elif player[0]['score']<player[1]['score']:     #玩家2胜利
        player[1]['is_win'] = True
        socketio.emit('server_response',
                      {'match': True, 'connect': True, 'type': 'finalResult', 'ready': True,
                       'winer': {'id': player[1]['account'], 'nick_name': player[1]['account'],'score':player[1]['score']}},
                      namespace='/compete', broadcast=True)
    else:                                           #两者平手
        player[0]['is_win'] = True
        player[1]['is_win'] = True
        socketio.emit('server_response',
                      {'match': True, 'connect': True, 'type': 'finalResult', 'ready': True,
                       'winer':None},
                      namespace='/compete', broadcast=True)
#time,score,isWin,rescueRightRate,structureRightRate,predictRightRate,correctNum

    # race_info=PlayerScore(time=data['score'],score=data['score'],isWin=player[1]['is_win'],rescueRightRate=data['contest_info']['rescueRate'],
    #                       structureRightRate=data['contest_info']['structureRate'],predictRightRate=data['contest_info']['predictRate'],correctNum=data['contest_info']['correct_num'])
    # race_info.caculateFinalInfo(id=session.get('account'))
@socketio.on('leave',namespace='/compete')
def on_leave(data):
    print('离开房间')
    username = data['user_id']
    player_pool.popPlayer(username)
    room=data['room']
    leave_room(room)
    close_room(room)
    print(username + ' has left the %s' % room)
    return {'data':'ok'}

@socketio.on('disconnect',namespace='/compete')
def handle_disconnect():
    player_pool.popPlayer()
    print('client disconnected')




#后台发送题目线程，判断此可是否应该发送题目信息
def background_thread(player_double_pool):
    # question_list=list(question_list)
    # print(len(question_list))
    # join_room(room)
    # print('%s and %s has entered the %s' % (player_list[0],player_list[1]))
    print('发送试题后台任务启动')
    question_list=player_double_pool[0][2]

    #发送第一道题
    socketio.emit('server_response',
                  {'match': True, 'connect': True, 'type': 'question', 'ready': True,
                   'data': question_list[0]}, namespace='/compete', broadcast=True)

    question_index = 1
    while True:
        # if player_double_pool[0]['current_index']==question_index and player_double_pool[1]['current_index']==question_index:      #题目序号一致时发送下一道题
        #     socketio.emit('server_response',
        #                   {'match': True, 'connect': True, 'type': 'question', 'ready': True,
        #                    'data': question_list[question_index]}, namespace='/compete', broadcast=True)
        #     continue
        if player_double_pool[0][0]['is_answer']==False or player_double_pool[0][1]['is_answer']==False:
            player_double_pool[0][0]['is_answer'] =True
            player_double_pool[0][1]['is_answer'] =True
            print('发送超时题目')
            question_index=player_double_pool[0][1]['current_index']
            if question_index==10:
                print('题目发送完毕，后台任务结束')
                break
            print(question_list[question_index])
            print('question_index为%s' %question_index)
            socketio.emit('server_response',
                          {'match': True, 'connect': True, 'type':'question','ready':True,'data': question_list[question_index]},namespace='/compete',broadcast=True)

