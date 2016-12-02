import re
import sqlite3
bool = False
list = ['APPLICATION FEE', 'APPLICATION DEADLINE', 'ACCEPTANCE RATE']
db = sqlite3.connect('Uni.sqlite3')
cur = db.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS UNIVERSITY '')
for i in list:
    for line in reversed(open("website.txt").readlines()):
        if bool is True:
            print tag[0] +': '+ line.strip()

        tag = re.findall(i, line)
        if len(tag) > 0:
            bool = True
            continue
        bool = False