from ..models.user import User
from ..models.person_game_info import PersonGameInfo
from ..models import mydb
from datetime import datetime
class UserRegister:
    def __init__(self,account,nick_name,password,tel):
        self.account=account
        self.nick_name=nick_name
        self.password=password
        self.tel=tel
        self.register_time=datetime.now()

    def verify_account(self):  # 校验账号合法性
        # 调用数据库类接口查询账号,默认返回False(数据库未查询到该账号，即未注册)
        if not User.query.filter_by(account=self.account).first():
            return True
        else:
            return False

    def commit_proIfo(self):  # 保存个人信息
        if self.verify_account() == True:
            try:
                user=User(account=self.account,nick_name=self.nick_name,avatar_path='avatar.png',password=self.password,tel=self.tel,register_time=self.register_time)
                user_game_info=PersonGameInfo(user_id=self.account)
                mydb.session.add(user)

                #注册成功后初始化成绩信息
                if mydb.session.commit()==None:
                    mydb.session.add(user_game_info)
                    mydb.session.commit()
                return {'status': True, 'is_login':False,'msg': 'Data insertion success'}
            except Exception as e:
                mydb.session.rollback()
                print(e)
                return {'status':False,'is_login':False,'msg':'Data insertion failed'}
        else:
            return {'status':True,'is_login':False,'msg':'Account had been exist'}

