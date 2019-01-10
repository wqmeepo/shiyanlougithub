# -*- coding: utf-8 -*-
import scrapy
import json
from shiyanlougithub.items import ShiyanlougithubItem

class GitPySpider(scrapy.Spider):
    name = 'git_py.py'
    start_urls = json.load(open('/home/shiyanlou/shiyanlougithub/shiyanlougithub/ipAddr.json')).values()
    def parse(self, response):
        for i in response.css('li.col-12'):
            yield ShiyanlougithubItem({
                'name': i.css('a::text').extract_first().strip(),
                'update_time': i.css('relative-time::attr(datetime)').extract_first()
                })
