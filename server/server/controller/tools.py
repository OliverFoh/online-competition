import json
from decimal import Decimal
from datetime import datetime,date
import os
import configparser
from queue import Queue
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(o, date):
            return o.strftime("%Y-%m-%d")
        elif isinstance(o, Decimal):
            return float(o)
        else:
            return json.JSONEncoder.default(self, o)

class AvatarUrlParser:
    def __init__(self):
        self.HOST=[{'name':'Tencent_cloud','ip':'129.28.101.21'},{'name':'localhost','ip':'127.0.0.1'}]
        self.my_config = configparser.ConfigParser()
        self.my_config.read(os.getcwd()+'/server/db.conf')
        # print(os.path.dirname(__file__))
        # print(os.getcwd())
    def getAbstractPath(self):
        if self.my_config.get('DB', 'HOST')==self.HOST[0]['ip']:
            return self.HOST[1]['ip']
        else:
            return self.HOST[0]['ip']
        #return 'haha'

if __name__ == '__main__':
    # print(os.path.join(os.getcwd(),'view/static/a.jpeg'))
    # my_config = configparser.ConfigParser()
    # test=AvatarUrlParser()
    # print(test.getAbstractPath())
    test=Queue()
    play_list=[{'name':'xiaoming','age':20},{'name':'Tom','age':19}]
    test.put(play_list)
    print(test.get())