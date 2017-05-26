# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ComingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_name=scrapy.Field()
    director=scrapy.Field()
    actor=scrapy.Field()
    type=scrapy.Field()
    poster=scrapy.Field()
    region=scrapy.Field()
    date=scrapy.Field()
    length=scrapy.Field()
    introduction=scrapy.Field()
    grade=scrapy.Field()
    comment_amount=scrapy.Field()
    herald=scrapy.Field()
    herald_img=scrapy.Field()
    imagelist=scrapy.Field()
    commentlist=scrapy.Field()
    content=scrapy.Field()

    pass
