import cfscrape
from BeautifulSoup import *
import re
import urllib

list = []
scraper = cfscrape.create_scraper()
html = scraper.get("http://premium.usnews.com/best-colleges/jhu-2077/applying").content
soup = BeautifulSoup(html)
print html
a = soup('a')
#for tag in a:


