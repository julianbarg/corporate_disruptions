# -*- coding: utf-8 -*-
import scrapy


class CpscSpider(scrapy.Spider):
    name = 'cpsc'
    allowed_domains = ['cpsc.gov/Recalls']
    start_urls = ['http://cpsc.gov/Recalls/']

    def parse(self, response):
        pass

        relative_next_page = response.xpath('//*[@class="next"]/a/@href').extract_first()
        if relative_next_page:
            absolute_next_page = response.urljoin(relative_next_page)
            yield Request(absolute_next_page, callback=self.parse)
