import eel
import sqlite3 
#іптортування необхідних бібліотек Python

eel.init('web') #підключення до каталогу /web

conn=sqlite3.connect(r"db/QuestionsDB.db")
cur=conn.cursor()
cur.execute("SELECT * FROM main;")
data=cur.fetchall()
#підключення до бази даних

class Question:
    def __init__(self, qnum=0, text=0):
        self.text=text
        self.qnum=qnum
    def display_info(self):
        print(f"Вопрос:{self.text}, является вопросом №{self.qnum}")
#клас питання. Має такі параметри як текст та номер питання

class Answer:
    def __init__(self, atrue=0, qnum=0, text=0):
        self.atrue=atrue
        self.qnum=qnum
        self.text=text
    def display_info(self):
        print(f"Ответ:{self.text}, относится к вопросу №{self.qnum}. Правильность: {self.atrue}")
#клас відпові. Має такі параметри як текст, правильний він чи ні, та до якого питання відноситься

question={}
answer={}
qkey=0
akey=0
#задання змінних необхідних у подальших діях

for i in data:
    if i[0]==1:
        question[qkey]=Question(qnum=i[2],text=i[3])
        qkey=qkey+1
    elif i[0]==0:
        answer[akey]=Answer(atrue=i[1],qnum=i[2],text=i[3])
        akey=akey+1
    else:
        pass
#присвоювання кожному запису із бази даних класу питання чи відповіді

f=open("web/index.html", "w", encoding="utf-8") #очищення файлу index.html для запису питань із бази даних
f.seek(0)
f.close
#очищення файлу index.html для запису питань із бази даних

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
#запис верхньої незмінної частини файла index.html

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
#запис кожного питання та усіх відповідей що до нього відносяться

htmlbottom=f'''
    </div>
          <div class="header" id="result"></div>
    <button type="button" onclick="count();block()">Закончить тест</button>  
    </div></div>
  </form>
  </div>
</body>
<script src="js/main.js"></script>
</html>'''
filea.write(htmlbottom)
#запис нижньої незмінної частини файла index.html

filea.close() #закриття файлу, тобто його збереження

@eel.expose
def CountQuestions():
    len_q=len(question)
    return len_q
#функція що рахує кількість питань та передає ії у JavaScript
CountQuestions() #визов функції

eel.start('index.html')#старт інтерфейсу програми написаного на html