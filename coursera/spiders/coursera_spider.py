# -*- coding: utf-8 -*-
import scrapy


class CourseraSpiderSpider(scrapy.Spider):
    name = 'coursera_spider'
    allowed_domains = ['https://pt.coursera.org/browse']
    start_urls = ['http://https://pt.coursera.org/browse/']

    def parse(self, response):
        pass
