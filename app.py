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

question=[]


print("gotovo")
