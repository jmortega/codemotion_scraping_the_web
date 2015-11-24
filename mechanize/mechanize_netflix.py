# imports
import mechanize
from bs4 import BeautifulSoup
# Create a Browser
b = mechanize.Browser()

# Disable loading robots.txt
b.set_handle_robots(False)

# Navigate
b.open('https://www.netflix.com/Login?locale=es-ES')

# Choose a form
b.select_form(nr=0)

# Fill it out
b['email'] = 'email'
b['password'] = 'password'

# Stubmit
fd = b.submit()

response =  fd.read()

# ... process the results
soup = BeautifulSoup(response,"lxml")
for link in soup.find_all('a'):
    print(link.get('href'))

