# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from postUGR.items import PostugrItem

class PostugrSpyderSpider(CrawlSpider):
    name = "postUGR_spyder"
    allowed_domains = ["osl.ugr.es"]
    start_urls = ['http://osl.ugr.es']

	# Patrón para las entradas que cumplan el formato de fecha aaaa/mm/dd
    rules = [Rule(LxmlLinkExtractor(allow=[r'\d{4}/\d{2}/\d{2}/*']),callback='process_response')]
	
    def process_response(self, response):
		item = PostugrItem()
		item['titulo'] = response.xpath("//h1/text()").extract()
		item['autor'] = response.xpath("//div[contains(@class, 'entry-meta')]//a[contains(@rel, 'author')]/text()").extract()
		item['contenido'] = response.xpath("//section[contains(@class, 'entry-content')]//p/text()").extract()
		item['categorias'] = response.xpath("//div[contains(@class, 'entry-meta')]/a[1]/text()").extract()
		item['etiquetas'] = response.xpath("//div[contains(@class, 'entry-meta')]/a/text()").extract()
		return item