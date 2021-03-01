from .question import Question
from ...models.user import User
from queue import Queue
from ..tools import AvatarUrlParser
import random
class Player:
    def __init__(self):
        self.player_queue=Queue()
        self.question=Question()
    def getQueue(self):
        return self.player_queue
    def pushPlayer(self,id):

        #从数据库调取详细信息
        result = User.query.filter_by(account=id).first()
        if result is not None:
            user={'account':id,
                  'nick_name':result.nick_name,
                  'avatar_url':AvatarUrlParser().getAbstractPath()+':5000/static/'+result.avatar_path}
            self.player_queue.put(user)
    def popPlayer(self):
        return self.player_queue.get()
    def printQueueNum(self):
        return self.player_queue.qsize()

    def getQuestionList(self):
        return self.question.getRandomQuestion()





if __name__ == '__main__':
    test=Player()
    test.pushPlayer('5')
    test.pushPlayer('2')
    print(test.printQueueNum())
    print(test.popPlayer())
