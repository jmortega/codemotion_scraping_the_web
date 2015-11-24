import requests 
from bs4 import BeautifulSoup 
page = requests.get('http://www.codemotion.es')
soup = BeautifulSoup(page.content,"lxml")
print "The title is " + str(soup.title.text)