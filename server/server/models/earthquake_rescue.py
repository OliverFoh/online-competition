#地震救援表
from . import mydb
class EarthquakeRescue(mydb.Model):
    __tableName__ = 'earthquake_rescue'
    id=mydb.Column(mydb.INT,nullable=False,primary_key=True,autoincrement=True)
    question_info=mydb.Column(mydb.JSON,nullable=True)
