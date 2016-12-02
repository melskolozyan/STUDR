import wikipedia
import sqlite3
from BeautifulSoup import *
import urllib


conn = sqlite3.connect('Copy.sqlite')
cur = conn.cursor()


def wikisearch(url):
    return 0
    pass


for i in range(1, 10):
    cur.execute('SELECT name FROM Names WHERE id = ?', (i, ))
    Uniname = str(cur.fetchone()[0])
    try:
        tup = wikisearch(url)
        cur.execute('''UPDATE Names SET students = (?) WHERE id = (?)''', (tup, i))
        print Uniname, i
    except: print ">>>ERROR<<<", Uniname, i
    # cur.execute('''UPDATE Names SET country =(?), locality = (?), students = (?) WHERE id = (?)''', (buffer(tup[2]), buffer(tup[1]), tup[0], i))

    conn.commit()
