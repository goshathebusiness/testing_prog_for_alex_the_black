class Question:
    def __init__(self, qnum=0, qtext=0): # qtype - question type   qnum - question number
        self.qtext=qtext
        self.qnum=qnum
    def display_info(self):
        print(f"Вопрос:{self.qtext}, является вопросом №{self.qnum}")

class Answer:
    def __init__(self, atype=0, atrue=0, qnum=0, atext=0): #atype - answer type   atrue - answer true   qnum - question number
        self.atype=atype
        self.atrue=atrue
        self.qnum=qnum
        self.atext=atext
    def display_info(self):
        print(f"Ответ:{self.atext}, относится к вопросу №{self.qnum}. Правильность: {self.atrue}")

#a=[(1,2,3,"coglacen"),(2,3,5,"necoglacen")]
#b={a[1]:"1"}
##a[1]=Question(qnum=a[2],qtext=a[3])
#question={"question1":"1","question2":"2"}
#question[1]=Question(qnum=2, qtext="aye")
#question[1].display_info
#a.display_info()

question={}
question[1]=Question(qnum=1,qtext="aye348")
question[2]=Question(qnum=2,qtext="aye562")
question[1].display_info()
question[2].display_info()

question[3]=Question(qnum=3,qtext="4443")
print(question)
print(len(question))