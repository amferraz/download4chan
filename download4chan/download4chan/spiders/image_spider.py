# coding: utf-8

from scrapy.spider import Spider
from scrapy.selector import Selector

from download4chan.items import ImagesItem


class ImageSpider(Spider):
    name = "images"
    allowed_domains = ["4chan.org"]
    start_urls = None

    def __init__(self, thread_url=''):
        self.start_urls = [thread_url]

    def parse(self, response):
        sel = Selector(response)
        hrefs = sel.css('a.fileThumb::attr(href)')

        imgs = ImagesItem()
        image_urls = []
        for a_href in hrefs:
            image_urls.append("http:%s" % a_href.extract())

        imgs['image_urls'] = image_urls
        yield imgs
