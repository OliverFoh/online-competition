from . import mydb
"""
-- person_game_info个人答题信息记录
-- 字段说明

-- user_id 用户id
-- level_grade 用户等级
-- integral_score 用户积分
-- win_rate 胜率（胜利次数/比赛次数）
-- win_num 胜利次数
-- last_isWin 上次比赛是否胜利
-- max_streak_num 最大连胜次数
-- streak_num 连胜次数
-- contest_num 比赛次数
-- average_score 平均成绩
-- average_time 平均用时
-- correct_rate 答题正确率
-- rescue_rate 救援知识答题正确率（本次正确率+以往正确率/总共比赛次数）
-- structure_rate 构造知识答题正确率
-- predict_rate 预测预警知识答题正确率

"""
class PersonGameInfo(mydb.Model):
    __tableName__='person_game_info'
    user_id=mydb.Column(mydb.VARCHAR(10),mydb.ForeignKey('user.account',ondelete='CASCADE',onupdate='CASCADE'),primary_key=True)
    level_grade=mydb.Column(mydb.SMALLINT,default=0)
    integral_score=mydb.Column(mydb.INT,default=0)
    win_rate=mydb.Column(mydb.DECIMAL(3,2),default=0.00)
    win_num=mydb.Column(mydb.INT,default=0)
    last_isWin=mydb.Column(mydb.BOOLEAN,default=True)
    max_streak_num = mydb.Column(mydb.INT, default=0)
    streak_num=mydb.Column(mydb.INT,default=0)
    contest_num=mydb.Column(mydb.INT,default=0)
    average_score = mydb.Column(mydb.DECIMAL(4,2), default=0)
    average_time = mydb.Column(mydb.DECIMAL(4,2), default=0)
    correct_rate=mydb.Column(mydb.DECIMAL(3, 2), default=0.00)
    rescue_rate = mydb.Column(mydb.DECIMAL(3, 2), default=0.00)
    structure_rate = mydb.Column(mydb.DECIMAL(3, 2), default=0.00)
    predict_rate = mydb.Column(mydb.DECIMAL(3, 2), default=0.00)




