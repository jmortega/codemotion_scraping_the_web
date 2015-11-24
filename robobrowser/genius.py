import re
from robobrowser import RoboBrowser

# Browse to Genius
browser = RoboBrowser(history=True)
browser.open('http://www.genius.com')

# Search for Porcupine Tree
#form = browser.get_form(action='/search')
#form = browser.get_form(class_='global_search global_search--giant')
#form = browser.get_forms()[0]
print form
form['q'].value = 'porcupine tree'
response = browser.submit_form(form)
print respo

# Look up the first song
songs = browser.select('.song_link')
browser.follow_link(songs[0])
lyrics = browser.select('.lyrics')
lyrics[0].text	

# Back to results page
browser.back()

# Look up my favorite song
song_link = browser.get_link('trains')
browser.follow_link(song_link)

# Can also search HTML using regex patterns
lyrics = browser.find(class_=re.compile(r'\blyrics\b'))
lyrics.text