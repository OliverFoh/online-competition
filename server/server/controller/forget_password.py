from ..models.user import User
class MissInfo:
    def __init__(self,account,nick_name,tel):
        self.account=account
        self.nick_name=nick_name
        self.tel=tel
    def getPassword(self):
        result = User.query.filter_by(account=self.account).first()
        if result is not None:
            if result.nick_name==self.nick_name and result.tel==self.tel:
                return {'status': True, 'is_login': False, 'password':result.password,'msg': 'get password  success'}
            else:
                return {'status':False,'is_login': False, 'msg': 'info error'}

