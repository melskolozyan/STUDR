import urllib
from BeautifulSoup import *
import re
import sqlite3
from google import google
import time

conn = sqlite3.connect('Copy.sqlite')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Info''')
cur.execute('''CREATE TABLE IF NOT EXISTS Info(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, country TEXT, locality TEXT, students INTEGER)''')

for i in range(1, 51):
    cur.execute('SELECT name FROM Names WHERE id = ?', (i, ))
    Uniname = str(cur.fetchone()[0])
    print Uniname
    wiki_results = google.search(Uniname + ' wikipedia', 1)
    time.sleep(2)
    wiki_link = wiki_results[0].link
    time.sleep(2)
    tup = wikisearch(wiki_link)
    cur.execute('''SELECT id FROM Names WHERE id = (?)''', (i, ))
    var = cur.fetchone()[0]
    print var
    cur.execute('''INSERT OR IGNORE INTO Info(country, locality, students) VALUES (?,?,?)''', (buffer(tup[2]), buffer(tup[1]), tup[0]))
    cur.execute('''SELECT id FROM Info WHERE students = ?''', (tup[0],))
    info_id = cur.fetchone()[0]
    cur.execute('''UPDATE Names SET info_id =(?) WHERE id =(?)''', (info_id ,i) )

    conn.commit()
    print tup
