#用户信息表
from . import mydb
class User(mydb.Model):
    __tableName__='user'
    account=mydb.Column(mydb.String(10),nullable=False,primary_key=True)
    avatar_path = mydb.Column(mydb.VARCHAR)
    nick_name = mydb.Column(mydb.String(20),nullable=False)
    password=mydb.Column(mydb.String(20),nullable=False)
    register_time=mydb.Column(mydb.DateTime)
    update_time=mydb.Column(mydb.DateTime)
    tel=mydb.Column(mydb.String(13))