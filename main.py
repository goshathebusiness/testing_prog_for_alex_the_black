import eel
import sqlite3

eel.init('web')

#@eel.expose # pered func for import in js

conn=sqlite3.connect(r"db/QuestionsDB.db")
cur=conn.cursor()
cur.execute("SELECT * FROM main;")
data=cur.fetchall()

class Question:
    def __init__(self, qnum=0, text=0): # qtype - question type   qnum - question number
        self.text=text
        self.qnum=qnum
    def display_info(self):
        print(f"Вопрос:{self.text}, является вопросом №{self.qnum}")

class Answer:
    def __init__(self, atrue=0, qnum=0, text=0): #atype - answer type   atrue - answer true   qnum - question number
        self.atrue=atrue
        self.qnum=qnum
        self.text=text
    def display_info(self):
        print(f"Ответ:{self.text}, относится к вопросу №{self.qnum}. Правильность: {self.atrue}")
print("ae")
print(data)
question={}
answer={}
qkey=0
akey=0

for i in data:
    if i[0]==1:
        question[qkey]=Question(qnum=i[2],text=i[3])
        qkey=qkey+1
    elif i[0]==0:
        answer[akey]=Answer(atrue=i[1],qnum=i[2],text=i[3])
        akey=akey+1
    else:
        print("Error")
    
print(question)
print(answer)

for i in range(len(question)):
    question[i].display_info()

for i in range(len(answer)):
    answer[i].display_info()



print("gotovo")
f=open("web/index.html", "w", encoding="utf-8")
f.seek(0)
f.close
filea=open('web/index.html','a', encoding="utf-8")

htmltop = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Тестуюча програма</title>

    <link rel="stylesheet" href="css/main.css">
    <script type="text/javascript" src="/eel.js"></script> 
</head>
<form>
<body>
<div class="parent">
<div class="table">
<div class="header">Тест з мови програмування Python</div>
<div>'''
filea.write(htmltop)
qalready=0
aalready=0

for i in range(len(question)):
    htmlloop_q=f'''
    </div>
    <div class="cell">
    <p>{i+1}. {question[i].text}</p>'''
    filea.write(htmlloop_q)
    for j in range(len(answer)):
        if answer[j].qnum==i:
            htmlloop_a=f'''
            <div class="block">
            <input type="radio" id="{j}"
            name="answer_for_question{i}" value="{answer[j].atrue}">
            <label for="{j}">{answer[j].text}</label>
            </div>'''
            filea.write(htmlloop_a)
        else:
            pass
    

htmlbottom=f'''
    </div>
          <div class="header" id="result"></div>
    <button type="button" onclick="count();block()">Закончить тест</button>  
    </div></div>
  </form>
  </div>
</body>
<script src="js/jquery-3.6.0.min.js"></script>
<script src="js/main.js"></script>
</html>'''
filea.write(htmlbottom)

filea.close()

@eel.expose
def CountQuestions():
    len_q=len(question)
    return len_q

CountQuestions()

eel.start('index.html')