#!/usr/bin/python2.7
__author__ = 'gargantua'

# anchor extraction from html document
from bs4 import BeautifulSoup
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import textwrap
from HTMLParser import HTMLParser

webpage = urllib2.urlopen('http://en.wikipedia.org/wiki/Main_Page')
soup = BeautifulSoup(webpage)
dyk_div = soup.find(id="mp-dyk")

ls = dyk_div.find_all('li')

def wrapper(s):
	return textwrap.fill(s, width=50)

for line,c in enumerate(ls):
	#if(line == int(sys.argv[1])):
	print wrapper(c.getText()) + "\n"
	if line > 4:
		break	

'''
for l in soup.find_all('li')
    print l'''

exit(1)