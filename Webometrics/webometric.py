import sqlite3
import cfscrape
from BeautifulSoup import *
import re
import time


file = sqlite3.connect('test.sqlite')
cur = file.cursor()
# cur.execute('''DROP TABLE IF EXISTS Names''')
cur.execute('''CREATE TABLE IF NOT EXISTS Names(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT, html TEXT)''')

for i in range(120):
    print "Parsing page number:", i
    url = 'http://www.webometrics.info/en/world?page='
    url = url + str(i)
    print url
    scraper = cfscrape.create_scraper()
    soup = BeautifulSoup(scraper.get(url).content)
    results = soup.findAll("a", {"target" : "_blank"})
    count = 1
    time.sleep(1)
    for tag in results:
        if count == 101: break
        html = tag.get('href')
        print html
        name =  str(tag.contents[0]).strip()
        if re.search('/', name):
            name = re.findall('(.*)/', name)[0].strip()
        name = buffer(name)
        print name

        # cur.execute('''INSERT OR IGNORE INTO Names(name, html) VALUES (?, ?)''', (name, buffer(html)))
        # file.commit()
        count += 1
