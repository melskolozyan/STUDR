import sqlite3
db = sqlite3.connect('Uni.sqlite3')
cur = db.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS UNIVERSITY ''')