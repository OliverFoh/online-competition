from server.models.user import User
from server.models.person_game_info import PersonGameInfo
from ..models import mydb
from .tools import DecimalEncoder,AvatarUrlParser
import json
from datetime import datetime
import uuid
import os
class UserInfo:
    def __init__(self,userId):
        self.userId=userId
    def getInfo(self):
        result = mydb.session.query(User,PersonGameInfo).filter(User.account==self.userId).filter(PersonGameInfo.user_id==self.userId).one()
        if result is not None:
            userInfo={
                'account':result[0].account,
                'nick_name':result[0].nick_name,
                'tel':result[0].tel,
                #等级
                'level_grade':result[1].level_grade,
                'integral_score':result[1].integral_score,
                'win_rate':json.dumps(result[1].win_rate ,cls=DecimalEncoder),
                'win_num':result[1].win_num,
                'max_streak_num':result[1].max_streak_num,
                'contest_num':result[1].contest_num,
                'correct_rate':str(result[1].correct_rate),
                'average_score':str(result[1].average_score),
                'average_time': str(result[1].average_time),
                'rescue_rate':str(result[1].rescue_rate),
                'structure_rate':str(result[1].structure_rate),
                'predict_rate':str(result[1].predict_rate)
            }
            # user['account']=result.account
            # user['nick_name']=result.nick_name
            print(type(result))
            print(result)
            print(result[0].nick_name)
            print(result[1].win_rate)
            return {'status':True,'is_login':True,'data':userInfo,'msg':'info fetch success'}
        else:
            return {'status':False,'is_login':True,'msg':'some error occured'}
    def modifyInfo(self,args):
        try:
            result = User.query.filter_by(account=self.userId).first()
            if result is not None:
                if 'new_password' in args:
                    result.password = args['new_password']
                if 'new_nick_name' in args:
                    result.nick_name = args['new_nick_name']
                if 'new_tel' in args:
                    result.tel = args['new_tel']
                result.update_time=datetime.now()
                mydb.session.commit()
            return {'status': True, 'is_login': True, 'msg': 'Data modify success'}
        except Exception as e:
            mydb.session.rollback()
            print(e)
            return {'status': False, 'is_login': True, 'msg': 'some error occured'}

    def modifyAvatar(self,avatarFile):
        base_path='server/view/static/'
        file = avatarFile
        print(file)
        try:
            randomFilePath=str(uuid.uuid1())+'.png'
            file.save(base_path+randomFilePath)
            print(os.path.abspath(os.path.join(os.getcwd())))
            result = User.query.filter_by(account=self.userId).first()
            if result is not None:
                if result.avatar_path!=None:
                    if result.avatar_path=='avatar.png':
                        #若未更换系统头像时直接跳过删除步骤
                        pass
                    else:
                        os.remove(os.getcwd()+'/'+base_path+result.avatar_path)
                        print('原头像已删除')
                result.avatar_path=randomFilePath
                mydb.session.commit()
                return {'status':True,'is_login':True,'avatarUrl':AvatarUrlParser().getAbstractPath()+':5000/static/'+randomFilePath,'msg': 'modify success'}
        except Exception as e:
            mydb.session.rollback()
            print(e)
            return {'status': False, 'is_login': True, 'msg': 'some error occured'}



