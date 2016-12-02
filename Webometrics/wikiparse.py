import urllib
from BeautifulSoup import *
import re

def wikilocation(url):
    soupfile = re.findall('Location<\/th>[\d\D]+<\/span><\/td>', html)[0]
    soup = BeautifulSoup(soupfile)
    country_tag = soup.findAll("span", {"class": "country-name"})
    locality_tag = soup.findAll("span", {"class": "locality"})
    country = country_tag[0].contents[0]
    locality = locality_tag[0].contents[0]

    if len(str(locality_tag[0].contents[0]).split()) > 1:
        locality = locality.contents[0]
    if len(str(country_tag[0].contents[0]).split()) > 1:
        country = country.contents[0]
    # print 'locality: ', locality, type(locality)
    # print 'country: ', country, type(locality)
    return (str(locality.encode('utf-8')), str(country.encode('utf-8')))

sample = 'https://en.wikipedia.org/wiki/University_of_Warwick'
html = urllib.urlopen(sample).read()
tup = wikilocation(sample)
print tup