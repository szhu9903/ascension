# -*- coding: utf-8 -*-
import re

import scrapy

class StocksSpider(scrapy.Spider):
    name = 'stocks'
    start_urls = ['http://quote.eastmoney.com/stock_list.html']

    def parse(self, response):
        for href in response.css('a::attr(href)').getall():
            try:
                stock = re.findall(r'[s][hz]\d{6}',href)[0].upper()
                url = 'https://xueqiu.com/S/'+stock
                yield scrapy.Request(url,callback=self.parse_stock)
            except:
                continue

    def parse_stock(self,response):
        stock_dict = {}
        stock_dict['stock_name'] = response.css('.stock-name').get()
        stock_dict['stock_current'] = response.css('.stock-current').get()
        yield stock_dict

