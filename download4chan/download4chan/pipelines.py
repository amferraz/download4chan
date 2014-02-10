# coding: utf-8

from scrapy.contrib.pipeline.images import ImagesPipeline


class Image4ChanDownloadPipeline(ImagesPipeline):
    def image_key(self, url):
        image_guid = url.split('/')[-1]
        return 'full/%s.jpg' % (image_guid)
