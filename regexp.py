import re
import urllib
from BeautifulSoup import *

text = urllib.urlopen('https://en.wikipedia.org/wiki/Harvard_University').read()


blah = re.findall('Location<\/th>[\d\D]+<\/span><\/td>', text)[0]
soup = BeautifulSoup(blah)
country_tag = soup.findAll("span", {"class" : "country-name"})
locality_tag = soup.findAll("span", {"class" : "locality"})
country = country_tag[0].contents[0]
locality = locality_tag[0].contents[0]

if len(str(locality_tag[0].contents[0]).split()) > 1:
    locality = locality.contents[0]
if len(str(country_tag[0].contents[0]).split()) > 1:
    country = country.contents[0]
print 'locality: ',locality
print 'country: ',country