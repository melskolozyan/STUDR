from BeautifulSoup import *
import urllib
import re
import sqlite3

file = sqlite3.connect('test.sqlite')
cur = file.cursor()
cur.execute('DROP TABLE IF EXISTS University')
cur.execute('''CREATE TABLE IF NOT EXISTS University (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
name VARCHAR(256),
fee VARCHAR(41),
total_enrollment VARCHAR(7),
scores_id INTEGER,
rank_id INTEGER
)''')
url = 'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/data'
count = 1
while True:
    print 'Parsing page #', count
    if count == 9: break
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
            if len(names) == 25: break
            link = str(item.get('href', ))
            if re.search('/best-colleges/.*-[0-9]+', link):
                names.append(str(item.contents[0]))
        a = str(tag.contents[0]).strip()
        try:
            if re.search('^[0-9]+,[0-9]+', a):
                total_enrollment = a
                if total_enrollment in total_enrollments:
                    done = True
                    break
                total_enrollments.append(total_enrollment)
            if re.search('\$[0-9]+?.*', a):
                fee = a
                fees.append(fee)
            # if re.search('N/A'):
        except:
            continue

    for i in range(len(names)):
        cur.execute('''INSERT INTO University(name, fee, total_enrollment) VALUES (?,?,?)''', (buffer(names[i]), buffer(fees[i]), buffer(total_enrollments[i])))
        file.commit()
    count = count + 1
    url = 'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/data/page+' + str(count)
