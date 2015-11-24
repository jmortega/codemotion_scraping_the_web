from Scraping import Scraping

if __name__ == "__main__":
	url = 'http://2015.codemotion.es'
	scraping = Scraping()
	scraping.scrapingImagesPdf(url)
	scraping.scrapingBeautifulSoup(url)