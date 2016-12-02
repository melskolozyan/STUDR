import re
import urllib
from BeautifulSoup import *
url = 'https://en.wikipedia.org/wiki/Harvard_University'

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

list = students(url)
for i in list:
    print i
