### A simple example of BeautifulSoup4 in Python ###
'''
This is a super simple example of using BeautifulSoup4 and Requests 
libraries in Python to parse a website page.
'''
import requests
from bs4 import BeautifulSoup

url="http://www.nytimes.com/"
r=requests.get(url)

# the output is not quite helpful
print (r.content)

# part of the result
'''
b'<!DOCTYPE html>\n<!--[if (gt IE 9)|!(IE)]> <!--> <html lang="en" class="no-js edition-domestic app-homepage"  
itemscope xmlns:og="http://opengraphprotocol.org/schema/"> <!--<![endif]-->\n<!--[if IE 9]> <html lang="en" class="no-js ie9 
lt-ie10 edition-domestic app-homepage" xmlns:og="http://opengraphprotocol.org/schema/"> <![endif]-->\n<!--[if IE 8]> 
<html lang="en" class="no-js ie8 lt-ie10 lt-ie9 edition-domestic app-homepage" xmlns:og="http://opengraphprotocol.org/schema/"> 
<![endif]-->\n<!--[if (lt IE 8)]> <html lang="en" class="no-js lt-ie10 lt-ie9 lt-ie8 edition-domestic app-homepage" xmlns:og=
"http://opengraphprotocol.org/schema/"> <![endif]-->\n<head>\n    <title>The New York Times - Breaking News, World News & 
Multimedia</title>\n   <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" /><script type="text/javascript">
window.NREUM||(NREUM={}),__nr_require=function(n,t,e){function r(e){if(!t[e]){var o=t[e]={exports:{}};n[e][0].call(o.exports,
function(t){var o=n[e][1][t];return r(o?o:t)},o,o.exports)}return t[e].exports}
'''

# apply BeautifulSoup to get the content
soup = BeautifulSoup(r.content,"lxml")
# now the output is more structured
print (soup.prettify())

# part of the result
'''
<!DOCTYPE html>
<!--[if (gt IE 9)|!(IE)]> <!-->
<html class="no-js edition-domestic app-homepage" itemscope="" lang="en" xmlns:og="http://opengraphprotocol.org/schema/">
 <!--<![endif]-->
 <!--[if IE 9]> <html lang="en" class="no-js ie9 lt-ie10 edition-domestic app-homepage" xmlns:og="http://opengraphprotocol.org/schema/"> <![endif]-->
 <!--[if IE 8]> <html lang="en" class="no-js ie8 lt-ie10 lt-ie9 edition-domestic app-homepage" xmlns:og="http://opengraphprotocol.org/schema/"> <![endif]-->
 <!--[if (lt IE 8)]> <html lang="en" class="no-js lt-ie10 lt-ie9 lt-ie8 edition-domestic app-homepage" xmlns:og="http://opengraphprotocol.org/schema/"> <![endif]-->
 <head>
  <title>
   The New York Times - Breaking News, World News &amp; Multimedia
  </title>
  <meta content="IE=edge,chrome=1" http-equiv="X-UA-Compatible"/>
  <script type="text/javascript">
'''

# explore the soup result a little, checking the title, paragrah, etc
print (soup.title)
print (soup.title.string)
print (soup.p)
print (soup.a)


# extracting all the URLs on NewYorkTimes's homepage
links = soup.find_all('a')
for link in links:
    print (link.get('href'))

# part of the result
'''
...
http://www.nytimes.com/upshot/
http://www.nytimes.com/2015/03/11/upshot/elizabeth-warren-is-no-barack-obama.html
http://www.nytimes.com/2015/03/11/upshot/women-on-boards-where-the-us-ranks.html
http://www.nytimes.com/2015/03/10/upshot/more-good-news-on-the-deficit-this-time-because-of-declining-private-insurance-costs.html
http://www.nytimes.com/pages/realestate/index.html
http://www.nytimes.com/2015/03/08/realestate/views-at-one57-for-29329100.html
http://www.nytimes.com/column/big-deal
http://realestate.nytimes.com/search/advanced.aspx
http://www.nytimes.com/ref/classifieds/
http://www.nytimes.com/2015/03/08/realestate/prewar-soho-loft-for-11-5-million.html
http://www.nytimes.com/2015/03/08/realestate/prewar-soho-loft-for-11-5-million.html
http://www.nytimes.com/gst/mostemailed.html
http://www.nytimes.com/gst/mostpopular.html
http://www.nytimes.com/recommendations
...
'''

# extracting all the text on the page
url2="http://www.goodreads.com/"
r2=requests.get(url2)
soup2 = BeautifulSoup(r2.content,"lxml")
print (soup2.get_text())



