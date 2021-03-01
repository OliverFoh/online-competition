from flask_restful import Resource,reqparse,request
from werkzeug.datastructures import FileStorage

from flask import session
from .controller.sign_in import UserLogin
from .controller.sign_up import UserRegister
from .controller.forget_password import MissInfo
from .controller.person_info import UserInfo
from .controller.match.robot_match import Roboter
from .controller.match.player_match import Player
from .controller.match.elo import UserRank
from .controller.session_auth import login_required

"""账号登录、注册、找回密码、登出接口"""
class Login(Resource):
    def __init__(self):
        #print(request.headers)
        self.login=UserLogin()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('account', type=str,required=True,location='args')
        self.parser.add_argument('password', type=str,required=True,location='args')
    def get(self):
        session.permanent=True
        args =self.parser.parse_args()
        if 'account' in session:
            print('%s已经登录' % session.get('account'))
            return {'status':True,'is_login':True,'msg':'Account has logged in'}
        response= self.login.query_account_password(account=args.get('account'),password=args.get('password'))
        if response['is_login']==True:
            session['account'] = args.get('account')
            print('%s成功登录' % session.get('account'))
        return response

class Register(Resource):
    def __init__(self):
        self.args=request.json
    def post(self):
        #print(request.form)
        self.register = UserRegister(account=self.args['account'], password=self.args['password'],
                                     nick_name=self.args['nick_name'], tel=self.args['tel'])
        response=self.register.commit_proIfo()
        return response

class Password(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('account', type=str, required=True, location='args')
        self.parser.add_argument('nick_name', type=str, required=True, location='args')
        self.parser.add_argument('tel', type=str, required=True, location='args')
        self.args=self.parser.parse_args()

    def get(self):
        user = MissInfo(account=self.args['account'],nick_name=self.args['nick_name'],tel=self.args['tel'])
        response=user.getPassword()
        return response


class LoginOut(Resource):

    def get(self):
        if 'account' in session:
            print('%s退出登录'% session.get('account'))
            session.pop('account')
            return {'status':True,'is_login':False,'msg':'Log out successfully'}
        else:
            return {'status':True,'is_login': False, 'msg': 'Please login'}





"""用户操作接口"""

#个人信息操作
class PersonalInfo(Resource):

    def __init__(self):
        print(session.get('account'))
        self.user = UserInfo(session.get('account'))

    @login_required
    def get(self):
        #print(request.headers)
        response=self.user.getInfo()
        #response={'account':session.get('account'),'msg':'success'}
        return response

    @login_required
    def post(self):
        args=request.json
        response=self.user.modifyInfo(args=args)
        return response

#修改个人头像
class PersonAvatar(Resource):
    @login_required
    def post(self):
        self.user = UserInfo(userId=session.get('account'))
        parser = reqparse.RequestParser()
        parser.add_argument('file', type=FileStorage, location='files')
        args = parser.parse_args()
        file = args['file']
        response=self.user.modifyAvatar(avatarFile=file)
        return response

""""""""""""""""""""""""
#机器人模式
class RobotMatch(Resource):
    #@login_required
    def get(self):
        #print(request.headers)
        self.robot=Roboter()
        question_list=self.robot.resolve()
        return {'status':True,'msg':'Question info fetch success','data':question_list}



class PlayerMatch(Resource):
    def __init__(self):
        self.player=Player()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('id', type=str, required=True)


    def get(self):
        args = self.parser.parse_args()
        if 'create_queue' in session:
            self.player.pushPlayer(args.get('id'))

        else:
            session['create_queue']=1
            self.player.createQueue()


""""""""""""""""""""""""""

#排行榜
class Rank(Resource):
    def __init__(self):
        self.args=request.args
        self.rank=UserRank(orderType=self.args.get('type'))
    def get(self):
        response=self.rank.orderByType()
        return response