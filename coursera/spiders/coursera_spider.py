# -*- coding: utf-8 -*-
import scrapy


class CourseraSpiderSpider(scrapy.Spider):
    name = 'coursera_spider'
    allowed_domains = ['*']
    start_urls = ['https://pt.coursera.org/browse?languages=en']

    def parse(self, response):
      categories_link = response.xpath("//a[contains(@class, 'DomainNavItem ')]")

      for category in categories_link:
        category_name = category.xpath(
          "span[contains(@class, 'domain-name')]/text()"
        ).extract()

        category_href = category.xpath("@href").extract()

        print(category_name, category_href)
