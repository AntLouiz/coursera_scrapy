# -*- coding: utf-8 -*-
import scrapy


class CourseraSpiderSpider(scrapy.Spider):
    name = 'coursera_spider'
    allowed_domains = ['*']
    start_urls = ['https://pt.coursera.org/browse?languages=en']
    root_url = 'https://www.coursera.org'

    def parse(self, response):
      categories_link = response.xpath("//a[contains(@class, 'DomainNavItem ')]")

      for category in categories_link:
        category_name = category.xpath(
          "span[contains(@class, 'domain-name')]/text()"
        ).extract()

        category_href = category.xpath("@href").extract_first()

        self.log("{}{}".format(self.root_url, category_href))

        request = scrapy.Request(
          url="{}{}".format(self.root_url, category_href),
          callback=self.parse_category,
          dont_filter=True
        )

        self.log(request)

        yield request

    def parse_category(self, response):
      self.log("ENTROU NO CALLBACK")
      self.log(response.xpath('//title/text()').extract_first())