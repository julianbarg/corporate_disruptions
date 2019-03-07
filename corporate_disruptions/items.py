# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class CpscItem(Item):
    name = Field()
    link = Field()
    hazard = Field()
    remedy = Field()
    date = Field()
    units = Field()
    description = Field()
    incidents = Field()
    retailer = Field()
    importer = Field()
    country = Field()

# class CorporateDisruptionsItem(Item):
#     # define the fields for your item here like:
#     # name = Field()
#     pass
