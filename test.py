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
tries=0
h=
#a.display_info()