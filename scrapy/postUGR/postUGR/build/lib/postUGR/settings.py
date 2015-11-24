# -*- coding: utf-8 -*-

# Scrapy settings for postUGR project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'postUGR'

SPIDER_MODULES = ['postUGR.spiders']
NEWSPIDER_MODULE = 'postUGR.spiders'

ITEM_PIPELINES = ['postUGR.pipelines.PostugrPipeline','postUGR.pipelines.CVSExport','postUGR.pipelines.XmlExportWithLabels','postUGR.pipelines.XmlExportWithOutLabels']


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'postUGR (+http://www.yourdomain.com)'
