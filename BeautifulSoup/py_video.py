#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bs4
from multiprocessing.pool import ThreadPool as Pool
import requests

root_url = 'http://pyvideo.org'
index_url = root_url + '/category/50/pycon-us-2014'

def get_video_page_urls():
	response = requests.get(index_url)
	#print response.text
	soup = bs4.BeautifulSoup(response.text,'lxml') 
	return [a.attrs.get('href') for a in soup.select('div#video-summary-content a[href^=/video]')]

def get_video_data(video_page_url):
	video_data = {}
	response = requests.get(root_url + video_page_url)
	soup = bs4.BeautifulSoup(response.text,'lxml')
	video_data['title'] = soup.select('div#videobox h3')[0].get_text()
	video_data['speakers'] = [a.get_text() for a in soup.select('div#sidebar a[href^=/speaker]')]
	video_data['youtube_url'] = soup.select('div#sidebar a[href^=http://www.youtube.com]')[0].get_text()
	
	# initialize counters
	video_data['views'] = 0
	video_data['likes'] = 0
	video_data['dislikes'] = 0
	
	try:
		video_data['youtube_url'] = soup.select('div#sidebar a[href^=http://www.youtube.com]')[0].get_text()
		response = requests.get(video_data['youtube_url'], headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36'})
		soup = bs4.BeautifulSoup(response.text,"lxml")
		video_data['views'] = int(re.sub('[^0-9]', '',soup.select('.watch-view-count')[0].get_text().split()[0]))
		video_data['likes'] = int(re.sub('[^0-9]', '',soup.select('#watch-like-dislike-buttons span.yt-uix-button-content')[0].get_text().split()[0]))
		video_data['dislikes'] = int(re.sub('[^0-9]', '',soup.select('#watch-like-dislike-buttons span.yt-uix-button-content')[2].get_text().split()[0]))
	except:
		# some or all of the counters could not be scraped
		pass
	return video_data
	
def show_video_stats():
	video_page_urls = get_video_page_urls()
	for video_page_url in video_page_urls:
		try:
			print video_page_url
			print(get_video_data(video_page_url))
		except:
			pass
		
print(get_video_page_urls())		
show_video_stats()