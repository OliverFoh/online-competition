from server.models import mydb
import json
import random
class Question:
    def __init__(self,cataglog_num=3,question_num=10):
        self.db=mydb
        self.cataglog_num=cataglog_num
        self.question_num=question_num

        #初始化数据表单列表
        self.tables=['earthquake_rescue','earthquake_structure','earthquake_predict']

    #创建不同分类题型抽取个数的数组
    def makeRandomList(self):
        random_list=[]
        max_range=self.question_num
        count=0
        for i in range(self.cataglog_num):
            if i ==self.cataglog_num-1:
                random_list.append(max_range)
                break
            random_list.append(random.randint(0,max_range))
            count+=random_list[i]
            max_range=self.question_num-count

        #再次随机打乱
        random.shuffle(random_list)
        return random_list

    #从数据库获取试题
    def getRandomQuestion(self):
        num_list=self.makeRandomList()
        #print(num_list)
        question_list=[]
        for i in range(len(num_list)):
            if num_list[i]==0:
                continue
            result=self.db.session.execute('select  question_info  from  %s order by rand() limit %s' %(self.tables[i],num_list[i]))

            for item in result:

                #print(type(item[0]))
                question_list.append(json.loads(item[0],encoding='utf-8'))

        # for item in question_list:
        #     print(item)

        #'SELECT question_info FROM earthquake_rescue WHERE id >= (SELECT floor(RAND() * (SELECT count(*) FROM earthquake_rescue))) ORDER BY id LIMIT 3;'


        return question_list
    def getSingleQuestion(self):
        random_index=random.randrange(0,3)
        result = self.db.session.execute(
            'select  question_info  from  %s order by rand() limit 1' % self.tables[random_index])
        for item in result:
            result=json.loads(item[0],encoding='utf-8')
        return result

