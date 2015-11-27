"""Example app to login to GitHub"""
import argparse
import mechanicalsoup
import getpass
import time

parser = argparse.ArgumentParser(description='Login to GitHub.')

username = raw_input ("Username: ")
password = getpass.getpass()

browser = mechanicalsoup.Browser()

# request github login page. the result is a requests.
#Response object http://docs.python-requests.org/en/latest/user/quickstart/#response-content
login_page = browser.get("https://github.com/login")

# login_page.soup is a BeautifulSoup object http://www.crummy.com/software/BeautifulSoup/bs4/doc/#beautifulsoup 
# we grab the login form
login_form = login_page.soup.select("#login")[0].select("form")[0]

# specify username and password
login_form.select("#login_field")[0]['value'] = username
login_form.select("#password")[0]['value'] = password

print login_form.select("#login_field")[0]['value']

# submit form
page = browser.submit(login_form, login_page.url)

counter = page.soup.find('span', class_='counter')
print "\nNumber repositories: " + counter.text

links = page.soup.findAll('a', class_='mini-repo-list-item')

for link in links:
	link_aux = link.select(".repo")
	link_aux = link_aux[0].text
	if not link_aux.startswith("https"):
		link_aux='https://github.com'+"/"+username+"/"+link_aux
	print "\n"+link_aux
	str = link_aux
	parts = str.split("/")
	user = parts[3]
	title = parts[4]

	pageAux = browser.get(link_aux)
	time.sleep(2)
	
	description = pageAux.soup.find('div', class_='repository-description')
	if description is not None and len(description)>0:
		print "Description: " + description.text.encode("utf-8").strip()
	
	authors = pageAux.soup.find('a', class_='user-mention')
	if authors is not None:
		for author in authors:
			print "Author: "+ author
			
	authors = pageAux.soup.find('a', class_='commit-author-section')
	if authors is not None:
		for author in authors:
			print "Author: "+ author
			
	authors = pageAux.soup.find('span', class_='user-mention')
	if authors is not None:
		for author in authors:
			print "Author: "+ author	
				
	enlaces = pageAux.soup.findAll('a')
	
	for enlace in enlaces:
		if enlace.get('href') == '/'+user+"/"+title+'/commits/master':
			print 'commits '+ enlace.select('span.num')[0].text.strip()
		if enlace.get('href') == '/'+user+"/"+title+'/branches':
			print 'branches '+ enlace.select('span.num')[0].text.strip()
		if enlace.get('href') == '/'+user+"/"+title+'/releases':
			print 'releases '+ enlace.select('span.num')[0].text.strip()
		if enlace.get('href') == '/'+user+"/"+title+'/graphs/contributors':
			print 'contributors '+ enlace.select('span.num')[0].text.strip()