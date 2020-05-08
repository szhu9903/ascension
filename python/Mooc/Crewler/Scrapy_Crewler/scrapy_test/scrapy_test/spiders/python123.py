# -*- coding: utf-8 -*-
import scrapy


class Python123Spider(scrapy.Spider):
    name = 'python123'
    allowed_domains = ['python123.io']
    start_urls = ['http://python123.io/']

    def parse(self, response):
        pass
