# Scrapy settings for download4chan project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'download4chan'

SPIDER_MODULES = ['download4chan.spiders']
NEWSPIDER_MODULE = 'download4chan.spiders'

USER_AGENT = 'download4chan (+github.com/amferraz/download4chan)'

TELNETCONSOLE_ENABLED = False

WEBSERVICE_ENABLED = False

ITEM_PIPELINES = {'download4chan.pipelines.Image4ChanDownloadPipeline': 1}

IMAGES_STORE = "./imgs/"
