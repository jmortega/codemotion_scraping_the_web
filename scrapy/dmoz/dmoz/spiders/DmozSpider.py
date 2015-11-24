from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from dmoz.items import Website

class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
    "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
    "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/",
    ]
    
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//ul/li')
        items = []
        for site in sites:
            item = Website()
            item['name'] = map(unicode.strip, site.select('a/text()').extract())
            item['url'] = map(unicode.strip, site.select('a/@href').extract())
            item['description'] = map(unicode.strip, site.select('text()').extract())
            items.append(item)
        return items
