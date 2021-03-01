from .question import Question
class Roboter:
    def __init__(self):
        self.question=Question()
    def resolve(self):
        question_json=self.question.getRandomQuestion()
        return question_json[0]


if __name__ == '__main__':
    test=Roboter()
    print(test.makeRandomList())
    #test.getRandomQuestion()



