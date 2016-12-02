from BeautifulSoup import *
import urllib
import re
import sqlite3

file = sqlite3.connect('test.sqlite')
cur = file.cursor()
# cur.execute('DROP TABLE IF EXISTS University')
cur.execute('''CREATE TABLE IF NOT EXISTS University (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
name VARCHAR(256),
fee VARCHAR(42),
total_enrollment VARCHAR(9),
scores_id INTEGER,
rank_id INTEGER
)''')

url = 'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/data/page+9'
html = urllib.urlopen(url)
soup = BeautifulSoup(html)
tdtags = soup('td') #the soup object that has the 'td' tags
soupa = BeautifulSoup(str(tdtags))
atags = soupa('a') #the soup object that has the 'a' tags that are within 'tg' tags
done = False
names = []
fees = []
total_enrollments = []
for tag in tdtags:
    if done == True: break
    for item in atags:
        if len(names) == 14: break
        link = str(item.get('href', ))
        if re.search('/best-colleges/.*-[0-9]+', link):
            names.append(str(item.contents[0]))
    a = str(tag.contents[0]).strip()
    try:
        if re.search('\$[0-9]+?.*', a):
            fee = a
            fees.append(fee)
        if re.search('^[0-9]+,[0-9]+', a) or re.search('N/A', a):
            if len(total_enrollments) == 14: break
            total_enrollment = a
            total_enrollments.append(total_enrollment)
    except:
        continue
for e in range(len(names)):
    try:
        f = names[e].split('&mdash;')
        names[e] = f[0] +'-'+ f[1]
    except: continue
# print len(names)
# print fees
# print len(fees)
# print total_enrollments
for i in range(14):
    print names[i], fees[i], total_enrollments[i]
    cur.execute('''INSERT INTO University(name, fee, total_enrollment) VALUES (?,?,?)''', (buffer(names[i]), buffer(fees[i]), buffer(total_enrollments[i])))
    file.commit()
