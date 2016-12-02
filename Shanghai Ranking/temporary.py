import urllib
from BeautifulSoup import *
import time
import re
import sqlite3

file = sqlite3.connect('1.sqlite')
cur = file.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS University(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
name VARCHAR(256),
foundyear VARCHAR(5),
total_enrollment VARCHAR(7)
)''')

#lines 18-32 return 2 lists, 1 contains all of the names and the other one has the href links
fn = open('blah.txt')
soup = BeautifulSoup(fn)
a = soup('a')
list = []
links = []
for tag in a: #This loop finds the names of the universities and appends them in order
    url = tag.get('href', None)
    if re.search('World-University-Rankings/.+html' , str(url)):
        list.append(str(tag.contents[0]))
        links.append(str(url))
for i in range(len(list)):
    if re.search('\n', list[i]): #This bit of code finds the U names that have \n in them and formats the string so its a asingle line
        uc = str(list[i])
        f = uc.split('\n')
        list[i] = f[0] + ' '+ f[1].strip()

for i in range((len(list))):
    cur.execute('''INSERT INTO University(name) VALUES (?)''',(buffer(list[i]), ))
    file.commit()

def function(links):
    service_url = 'http://www.shanghairanking.com/'
    id = int(raw_input('>>>'))
    tries = 1
    temp_year = None
    temp_enrollment = None
    i = id - 1
    while True:
        try:
            url = service_url + links[i]
            print id
            html = urllib.urlopen(url)
            print '=====Opened the page====='
            html = html.read()
            print '=====Page Read====='
        except:
            print '----Failed to retrieve----', url
            tries += 1
            print '----Reattempting-----', 'Attempt#' + str(tries)
            if tries == 5: break
            time.sleep(2)
            continue
        print 'Successfully retrieved', url
        soup = BeautifulSoup(html)
        tags = soup('td')
        enroll = soup('p')
        found = False
        for tag in tags:
            if found:
                try: temp_year = str(tag.contents[0])
                except: temp_year = ' '
                print 'Added the year', temp_year
                break
            if str(tag.contents[0]) == 'Found Year:':
                found = True
                continue
        enrollfind = False
        for t in enroll:
            if re.search('Enrollment:', str(t)):
                enrollfind = True
                temp_enrollment = str(t.contents[0].split(':')[1])
                print 'Added the total enrollment number', str(t.contents[0].split(':')[1])
                break
        if enrollfind == False:
            temp_enrollment = 'N/A'
            print 'Added the total enrollment number', 'N/A'
        cur.execute('''UPDATE University SET foundyear = ?, total_enrollment = ? WHERE id =?''', (temp_year, temp_enrollment, id))
        file.commit()
        print 'Added', temp_year, 'and', temp_enrollment, 'to id', id
        id = id + 1
        i = id - 1

function(links)