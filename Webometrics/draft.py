import urllib
from BeautifulSoup import *
import sqlite3
import re
import wikipedia

def students(url):
    try:  #Tries finding the seperate undergraduate and graduate student counts and returns undergrad, grad and total student numbers as a list
        html = urllib.urlopen(url).read()
        undhtml = re.findall('Undergraduates</a>[\d\D]+</td>', html)[0]
        soup = BeautifulSoup(undhtml)
        tags = soup('td')
        undergrad = int(str(tags[0].contents[0]).replace(',', '').split()[0])
        # print undergrad

        gradhtml = re.findall('Postgraduates</a>[\d\D]+</td>', html)[0]
        soup = BeautifulSoup(gradhtml)
        tags = soup('td')
        grad = int(str(tags[0].contents[0]).replace(',', '').split()[0])
        # print grad
        return [undergrad, grad, undergrad+grad]
    except: #If something failes in the above code(most likely no undergrad and grad tabs) tries finding the total number of students
        totalhtml = re.findall('Students</th>[\d\D]+</td>', html)[0]
        soup = BeautifulSoup(totalhtml)
        tags = soup('td')
        total = int(str(tags[0].contents[0]).replace(',', ''))
        return [None, None, total]

conn = sqlite3.connect('Copy.sqlite')
cur = conn.cursor()
for i in range(998, 1001):
    cur.execute('SELECT name FROM Names WHERE id = ?', (i, ))
    Uniname = str(cur.fetchone()[0])
    wikiurl = wikipedia.page(wikipedia.search(Uniname)[0]).url
    try:
        list = students(wikiurl)
        print '>>>#'+str(i) ,Uniname
        print 'Undergraduates: ', list[0]
        print 'Graduates: ', list[1]
        print 'Total: ', list[2]
    except:
        print 'ERROR'
        continue