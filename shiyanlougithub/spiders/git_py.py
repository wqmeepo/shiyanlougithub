# -*- coding: utf-8 -*-
import scrapy
import json
from shiyanlougithub.items import ShiyanlougithubItem

class GitPySpider(scrapy.Spider):
    name = 'git_py.py'
    start_urls = ['https://github.com/shiyanlou?tab=repositories']
    def parse(self, response):
        for i in response.css('li.col-12'):
            item = ShiyanlougithubItem()
            item['name'] = i.css('a::text').extract_first().strip()
            item['update_time'] = i.css('relative-time::attr(datetime)').extract_first()
            course_url = response.urljoin(i.xpath('.//a/@href').extract_first())
            request = scrapy.Request(course_url,callback = self.parse_inter)
            request.meta['item'] = item
            yield request
        url = response.xpath('//div[@class="pagination"]//@href').extract_first()
        yield response.follow(url, callback= parse)

    def parse_inter(self, response):
        item = request['item']
        item['commits'] = response.xpath('//span[@class="num text-emphasized"]/text()').extract()[0].strip()
        item['branches'] = response.xpath('//span[@class="num text-emphasized"]/text()').extract()[0].strip()
        item['releases'] = response.xpath('//span[@class="num text-emphasized"]/text()').extract()[2].strip()
        yield item 
