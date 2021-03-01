# 地震结构知识表
from . import mydb
class EarthquakeStructure(mydb.Model):
    __tableName__='earthquake_structure'
    id = mydb.Column(mydb.INT, nullable=False, primary_key=True, autoincrement=True)
    question_info = mydb.Column(mydb.JSON, nullable=True)
