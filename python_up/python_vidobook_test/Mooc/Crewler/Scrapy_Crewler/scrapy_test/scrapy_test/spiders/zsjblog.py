# -*- coding: utf-8 -*-
import scrapy

class ZsjblogSpider(scrapy.Spider):
    name = 'zsjblog'
    start_urls = ['https://zsjblog.com/index']


    def parse(self, response):
        path = 'E:\jiandan\scrapy\\'
        fname = response.url.split('/')[-1]+'.html'
        path_name = path+fname
        with open(path_name,'wb') as f:
            f.write(response.body)
            f.close()
        self.log('SAVE file %s'%fname)



