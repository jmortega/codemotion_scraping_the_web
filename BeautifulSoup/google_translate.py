#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import sys

#Example input to enter : en (= english)
convert_from = raw_input("Language to Convert from : ")

#Example input to enter : hi (= hindi), fr (= french), de (= German)
convert_to = raw_input("Language to Convert to : ")

#Example input to enter : Hello World
text_to_convert = raw_input("Text to Convert : ")

#A url cannot have spaces as parameters, so we replace all the spaces with '+'
text_to_convert = text_to_convert.replace(' ', '+')

#Passing the parameters to service
url = 'http://translate.google.com/?sl=%s&tl=%s&text=%s' % (convert_from, convert_to, text_to_convert)

#Get the content
data = requests.get(url).content

#For unicode support use this.
soup = BeautifulSoup(data, "lxml")

#Getting the result which is in div gt-res-content and inside that its in span result_box's text. Use Firebug to check this.
div_content = soup.find('div', {'id' : 'gt-res-content'})
converted_text = div_content.find('span', {'id':'result_box'}).text

print "Converted Text : " + converted_text
