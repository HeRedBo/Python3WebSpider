# -*- coding: utf-8 -*-
import scrapy
from  scrapy import Spider, Request
from urllib.parse import urlencode
import json
from images360.items import Images360Item


class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['image.so.com']
    start_urls = ['http://image.so.com/']

    def start_requests(self):
        data = {'ch': 'beauty', 'listtype': 'new', 'temp':1 }
        base_url = "https://image.so.com/zj?"
        for page in range(1, self.settings.get("MAX_PAGE") + 1):
            data['sn'] = page * 30
            params = urlencode(data)
            url = base_url + params
            yield Request(url, self.parse)

    def parse(self, response):
        result = json.loads(response.text)
        for image in result.get('list'):
            item = Images360Item()
            item['id'] = image.get('id')
            item['title'] = image.get('group_title')
            item['url'] = image.get('qhimg_url')
            item['thumb'] = image.get('qhimg_thumb_url')
            yield item

