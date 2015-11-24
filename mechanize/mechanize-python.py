import re
import mechanize

br = mechanize.Browser()
br.set_handle_robots(False)
br.open("http://www.python.org")
print br.response().read()

for link in br.links(url_regex="python.org"):
	print link
	# follow second link with element text matching regular expression
	response = br.follow_link(link)
	print br.title()
	print response.geturl()
	print response.info() # headers
	print response.read() # body
	br.back()