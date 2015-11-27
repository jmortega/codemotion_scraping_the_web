#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json 
from bs4 import BeautifulSoup
import requests

base_url ='http://www.acec.ca/about_acec/search_member_firms/business_sector_search.html/search/business/page/%s'

url = base_url % 1
page = requests.get(url)
soup = BeautifulSoup(page.content,"lxml")
table = soup.find(id='resulttable')
rows = table.find_all('tr')
columns = rows[0].find_all('td')


company_data ={
	'name': columns[1].a.text,
	'id': columns[1].a['href'].split('/')[-1],
	'location': columns[2].text
}

start_page =1
end_page =2
result = []

for i in range(start_page,end_page +1):
	url = base_url % i
	print "Fetching %s" % url
	page = requests.get(url)
	soup = BeautifulSoup(page.content,"lxml")
	table = soup.find(id='resulttable')
	rows = table.find_all('tr')
	for r in rows: 
		columns = r.find_all('td')
		company_data ={
			'name': columns[1].a.text,
			'id': columns[1].a['href'].split('/')[-1],
			'location': columns[2].text
		}
		result.append(company_data)
	
with open('acec.json','w') as outfile:
	json.dump(result,outfile)	
