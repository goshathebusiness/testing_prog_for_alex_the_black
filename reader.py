from ast import parse
from cgitb import html
from unicodedata import name
import eel
import sqlite3
import urllib3
import urllib

eel.init('web') # ne ebu
#eel.start('index.html') # v konce
#@eel.expose # pered func for import in js

conn=sqlite3.connect(r"db/Input.db")
cur=conn.cursor()
cur.execute("SELECT * FROM main;")
data=cur.fetchall()

@eel.expose
def read_values():
    url = 'web/reader.html'
    values = {'q' : '[python]'}
    data = urllib.urlencode(values)
    req = urllib3.Request(url, data)
    response = urllib3.urlopen(req)
    html445 = response.read()
    print (html445)

@eel.expose
def count_true(num_true)->int:
    num_true_p=num_true
    return num_true_p


eel.start('reader.html')