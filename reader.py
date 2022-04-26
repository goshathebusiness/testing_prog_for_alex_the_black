from ast import parse
from cgitb import html
from unicodedata import name
import eel
import sqlite3

eel.init('web') # ne ebu
#eel.start('index.html') # v konce
#@eel.expose # pered func for import in js

conn=sqlite3.connect(r"db/Input.db")
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

print(question[2].text)

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Eel example</title>

    <link rel="stylesheet" href="css/main.css">
    <script type="text/javascript" src="/eel.js"></script> 
</head>
<body>
  <h1>It's {question[2].text} </h1>
</body>
</html>'''

with open('web/reader.html','w') as file:
  file.write(html)

eel.start('reader.html')