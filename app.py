from cgitb import html
import eel
import random
from datetime import datetime
import sqlite3

eel.init('web')
conn=sqlite3.connect("db/QAdb.db")
cursor=conn.cursor()

questions = []
answers = []
questions_value_already = 1
answers_value_already = 1  
questions_value_desired=0  
answers_value_desired=0

#default

@eel.expose
def settings():
    questions_value_desired = input("Введите желаемое количество вопросов: ")
    while type(questions_value_desired) != int:
        try:
            questions_value_desired = int(questions_value_desired)
        except:
            questions_value_desired = input("Введите целое число: ")
    answers_value_desired = input("Ответов на один вопрос: ")
    while type(answers_value_desired) != int:
        try:
            answers_value_desired = int(answers_value_desired)
        except:
            answers_value_desired = input("Введите целое число: ")
    return questions_value_desired,answers_value_desired

@eel.expose
def new_question():
    global questions
    global answers
    global questions_value_already
    global answers_value_already
    questions_def = {}
    answers_def = {}
    answer_value_def = 1
    questions_def = input("Введите вопрос: ")
    print(questions_value_already, "/", questions_value_desired)
    questions.append(questions_def)
    questions_value_already = questions_value_already+1
    while answer_value_def <= answers_value_desired:
        answers_def = input("Введите ответ ")
        print(answer_value_def, "/", answers_value_desired)
        answers.append(answers_def)
        answers_value_already = answers_value_already+1
        answer_value_def = answer_value_def+1

@eel.expose
def write_in_file():
    output=open("output.txt",mode="w", encoding="utf-8")
    output.writelines(questions_value_already)
    output.writelines(answers_value_desired)
    while len(questions)>0:
        questions_written=[]
        answers_written=[]
        questions_written=questions.pop(0)
        questions_written=str(questions_written)+"\n"
        output.writelines(questions_written)
        answers_written.append(answers.pop(0))
        answers_written.append(answers.pop(0))
        answers_written.append(answers.pop(0))
        print(answers_written)
        for i in answers_written:
            i=str("   "+i+"\n")
            output.writelines(i)
    print("Запись произведена")
    output.close

@eel.expose
def start():
    global questions_value_desired
    global answers_value_desired
    global answers_value
    print("1 - Задать вопросы")
    print("2 - Скомпилировать файл")
    start_number = input("Введите значение: ")
    while type(start_number) != int:
        try:
            start_number = int(start_number)
        except:
            start_number = input("Введите целое число: ")
    if start_number == 1:
        questions_value_desired, answers_value_desired = settings()
        answers_value = questions_value_desired*answers_value_desired
        while questions_value_already<=questions_value_desired:
            new_question()
        write_in_file()
        return
    elif start_number == 2:
        print("4444")
    else:
        return

eel.start('index.html')

conn.commit
conn.close