from BeautifulSoup import *
import urllib
import re
# from google import google

url ='http://www.prepscholar.com/sat/s/colleges/Syracuse-University-SAT-scores-GPA'

def prepscholar(url):
    # search_results = google.search(url , 1)
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('h2')
    for tag in tags:
        line1 = tag.contents[0]
        if re.search('Average SAT', line1):
            a = line1.split('SAT:')[1].strip().split('(New:') #es 2 printeri texy petqa linen db lcnox koder@
            print int(a[0])
            print int(re.findall('[0-9]+', a[1])[0])
        if re.search('Average GPA', line1):
            print float(line1.split('GPA:')[1].strip())
prepscholar(url)