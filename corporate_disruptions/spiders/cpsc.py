# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.loader import ItemLoader
from scrapy.http import Request

from corporate_disruptions.items import CpscItem


class CpscSpider(Spider):
    name = 'CpscSpider'
    allowed_domains = ['cpsc.gov']
    start_urls = ['http://cpsc.gov/Recalls/']

    def parse(self, response):
        recalls = response.xpath('//*[@class="view-content"]/div')
        for recall in recalls:
            relative_recall_url = recall.xpath('.//a/@href').extract_first()
            absolute_recall_url = response.urljoin(relative_recall_url)
            yield Request(absolute_recall_url, callback=self.parse_recall)

        relative_next_page = response.xpath('//*[@class="next"]/a/@href').extract_first()
        if relative_next_page:
            absolute_next_page = response.urljoin(relative_next_page)
            yield Request(absolute_next_page, callback=self.parse)

    def parse_recall(self, response):
        loader = ItemLoader(item=CpscItem())
        loader.add_value('link', response.url)

        name = response.xpath('//*[contains(text(), "Name of product:")]/following-sibling::*/text()').extract_first()
        loader.add_value('name', name)

        hazard = response.xpath('//*[contains(text(), "Hazard:")]/following-sibling::*//text()').extract_first()
        loader.add_value('hazard', hazard)

        remedy = response.xpath('//*[contains(text(), "Remedy:")]/following-sibling::*/text()').extract_first()
        loader.add_value('remedy', remedy)

        date = response.xpath('//*[contains(text(), "Recall date:")]/following-sibling::*/text()').extract_first()
        loader.add_value('date', date)

        units = response.xpath('//*[contains(text(), "Units: ")]/following-sibling::*//text()').extract()
        units = '\n'.join(units)
        loader.add_value('units', units)

        description = response.xpath('//*[contains(text(), "Description:")]/following-sibling::div//p/text()')\
            .extract_first()
        loader.add_value('description', description)

        incidents = response.xpath('//*[contains(text(), "Incidents/Injuries:")]/following-sibling::*//text()')\
            .extract_first()
        loader.add_value('incidents', incidents)

        retailer = response.xpath('//*[contains(text(), "Sold At:")]/following-sibling::*//text()').extract_first()
        loader.add_value('retailer', retailer)

        importer = response.xpath('//*[contains(text(), "Importer(s):")]/following-sibling::*//text()').extract_first()
        loader.add_value('importer', importer)

        country = response.xpath('//*[contains(text(), "Manufactured In:")]/following-sibling::*//text()')\
            .extract_first()
        loader.add_value('country', country)

        yield loader.load_item()
