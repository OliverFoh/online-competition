#地震预测预警信息表
from . import mydb
class EarthquakePredict(mydb.Model):
    __tableName__ = 'earthquake_predict'
    id=mydb.Column(mydb.INT,nullable=False,primary_key=True,autoincrement=True)
    question_info=mydb.Column(mydb.JSON,nullable=True)