from ..models.user import User
from ..controller.tools import AvatarUrlParser
class UserLogin:
    def __init__(self):
        pass
    def query_account_password(self,account,password):
        result= User.query.filter_by(account=account).first()
        # data=User.query.all()
        # for item in data:
        #     print(item.question_info)
        if result is not None:
            if result.password==password:
                user={
                    'account':result.account,
                    'nick_name':result.nick_name,
                    'avatarUrl':AvatarUrlParser().getAbstractPath()+':5000/static/'+result.avatar_path
                }
                return {'status':True,'is_login':True,'user':user,'msg':'Login  success'}
            else:
                return {'status':True,'is_login': False, 'msg': 'Password error'}
        else:
            return {'status':True,'is_login':False,'msg':'Account not exist'}

    def post(self):
        return 'false'



