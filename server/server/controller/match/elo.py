from ...models.user import User
from ...models.person_game_info import PersonGameInfo
from ...models import mydb
from ..tools import AvatarUrlParser
"""排行榜类"""
class UserRank:
    def __init__(self,orderType='max_streak_num',limit_num=5):
        self.orderType=orderType
        self.limit_num=limit_num
        self.db=mydb
    #按照对应的需求排名
    def orderByType(self):
        try:
            result=self.db.session.execute('select  user_id,%s  from  person_game_info order by %s DESC LIMIT %s' %(self.orderType,self.orderType,self.limit_num))
            if result is not None:
                rank_list=[]
                for item in result:
                    user={}
                    user['user_id']=item.user_id
                    userInfo=User.query.filter_by(account=item.user_id).first()
                    user['nick_name']=userInfo.nick_name
                    user['avatarUrl'] = AvatarUrlParser().getAbstractPath()+':5000/static/'+userInfo.avatar_path
                    if self.orderType=='max_streak_num':
                        user['max_streak_num']=item.max_streak_num
                    else:
                        user['win_rate']=str(item.win_rate)
                    rank_list.append(user)
                return {'status':True,'data':rank_list,'msg':'fetch success'}
        except Exception as e:
            print(e)
            return {'status': False, 'msg': 'some errors occured'}


"""玩家成绩信息处理类"""
"""
-- user_id 用户id
-- level_grade 用户等级
    200、400、700、1100、1600
-- integral_score 用户积分
-- win_rate 胜率（胜利次数/比赛次数）
-- win_num 胜利次数
-- max_streak_num 最大连胜次数
-- contest_num 比赛次数
-- average_score 平均成绩
-- average_time 平均用时
-- correct_rate 答题正确率
-- rescue_rate 救援知识答题正确率（本次正确率+以往正确率/2）
-- structure_rate 构造知识答题正确率
-- predict_rate 预测预警知识答题正确率
-- last_isWin 上次比赛是否胜利
-- streak_num  连胜次数
"""
class PlayerScore:
    def __init__(self,time,score,isWin,rescueRightRate,structureRightRate,predictRightRate,correctNum):
        self.time=time  #完成耗时
        self.score=score  #成绩
        self.isWin=isWin    #是否胜利
        self.rescueRightRate=rescueRightRate  #救援知识正确率
        self.structureRightRate=structureRightRate    #构造知识正确率
        self.predictRightRate=predictRightRate        #预测知识正确率
        self.correctNum=correctNum          #总共正确个数
        self.db=mydb
    def caculateFinalInfo(self,id):
        try:
            result = PersonGameInfo.query.filter_by(account=id).first()
            if result is not None:

                #比赛次数更新
                result.contest_num += 1
                if result.contest_num==0:
                    # 平均得分
                    result.average_score = round(self.score)

                    # 平均用时
                    result.average_time = round(self.time)

                    # 答题正确率
                    result.correct_rate = round(self.correctNum / 10)

                    # 救援知识正确率
                    result.rescue_rate = round(self.rescueRightRate)

                    # 预测知识正确率
                    result.predict_rate = round(self.predictRightRate)

                    # 构造知识正确率
                    result.structure_rate = round(self.structureRightRate)

                #已有过比赛记录时

                # 平均得分
                result.average_score=round((self.score+result.average_score)/2,2)

                #平均用时
                result.average_time=round((self.time+result.average_time)/2,2)

                #答题正确率
                result.correct_rate=round((result.correct_rate+(self.correctNum/10))/2,2)

                #救援知识正确率
                result.rescue_rate=round((result.rescue_rate+self.rescueRightRate)/2,2)

                #预测知识正确率
                result.predict_rate=round((result.predict_rate+self.predictRightRate)/2,2)

                #构造知识正确率
                result.structure_rate=round((result.structure_rate+self.structureRightRate)/2,2)





                    #当前局胜利时
                if self.isWin==True:
                    #更新胜利状态
                    result.last_isWin=self.isWin

                    # 胜利场数增加
                    result.win_num+=1

                    #胜率更新
                    result.win_rate = (result.win_num + 1) / (result.contest_num + 1)


                    if result.last_isWin==True:
                        result.streak_num=result.streak_num+1       # 连胜次数+1
                        if result.streak_num+1>result.max_streak_num:   #大于最大连胜次数时更新
                            result.max_streak_num=result.streak_num+1
                        result.integral_score = result.integral_score + self.score + (result.streak_num + 1) * 10   # 积分更新

                    if result.last_isWin==False:
                        result.integral_score = result.integral_score + self.score

                    #当前局失败时
                if self.isWin==False:
                    # 更新胜利状态
                    result.last_isWin = self.isWin

                    #胜率更新
                    result.win_rate=result.win_num/(result.contest_num+1)

                    result.streak_num = 0  # 连胜次数更新
                    result.integral_score = result.integral_score + self.score   # 积分更新
            self.db.session.commit()
        except Exception as e:
            self.db.session.rollback()
            print(e)

#比赛记录
class ContestRecord:
    def __init__(self,userA,userB):
        self.userA=userA
        self.userB=userB
        self.db=mydb
    def insertContestRecord(self):
        print()



