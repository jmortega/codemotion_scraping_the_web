# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy import signals
from scrapy.contrib.exporter import CsvItemExporter
from scrapy.contrib.exporter import XmlItemExporter
import codecs
import json
import csv

class PostugrPipeline(object):
    def __init__(self):
        self.file = codecs.open('postUGR_items.json', 'w+b', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()
		

class CVSExport(object):

    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
         pipeline = cls()
         crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
         crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
         return pipeline

    def spider_opened(self, spider):
        file = open('postUGR_items.csv', 'w+b')
        self.files[spider] = file
        self.exporter = CsvItemExporter(file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
    	self.exporter.export_item(item)
    	return item
		
class XmlExportWithLabels(object):

    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
         pipeline = cls()
         crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
         crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
         return pipeline

    def spider_opened(self, spider):
        file = open('postUGR_withLabel.xml', 'w+b')
        self.files[spider] = file
        self.exporter = XmlItemExporter(file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
		self.exporter.finish_exporting()
		file = self.files.pop(spider)
		file.close()
		
		#Construcción de la tabla html
		ficheroHTML = open('postUGR_items.html', "w")
		ficheroHTML.write("<!DOCTYPE html>\n<html>\n<header>\n<title>Fichero CSV a HTML</title>\n</header>\n<body>\n<table border=\"1\">\n")
       
		hdlFicheroCSV = open('postUGR_items.csv', "rb")
		objFilaCSV = csv.reader(hdlFicheroCSV)
		rownum = 0
		header = "Campo"
		for row in objFilaCSV:
			ficheroHTML.write("<tr>")
			colnum = 0
			for col in row:
				ficheroHTML.write("<td>")
				ficheroHTML.write(col)
				ficheroHTML.write("</td>")
				colnum += 1
		ficheroHTML.write("</tr>")      
		rownum += 1
		ficheroHTML.write("</table>\n</body>\n</html>")
		ficheroHTML.close()
			
    def process_item(self, item, spider):
    	if item['etiquetas']:
    		self.exporter.export_item(item)
    	return item

class XmlExportWithOutLabels(object):

    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
         pipeline = cls()
         crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
         crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
         return pipeline

    def spider_opened(self, spider):
        file = open('postUGR_withOutLabel.xml', 'w+b')
        self.files[spider] = file
        self.exporter = XmlItemExporter(file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
    	if not item['etiquetas']:
    		self.exporter.export_item(item)
    	return item
		

