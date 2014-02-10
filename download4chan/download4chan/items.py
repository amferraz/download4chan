# coding: utf-8

from scrapy.item import Item, Field


class ImagesItem(Item):
    image_urls = Field()
