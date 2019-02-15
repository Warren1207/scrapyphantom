# -*- coding: utf-8 -*-

import scrapy
from scrapyphantom.items import ScrapyphantomItem

class KpdSpider(scrapy.Spider):
    name = 'kpd'
    allowed_domains = ['kpd374.com']
    start_urls = ['https://www.kpd374.com/whmm/index.html']

    def parse(self, response):
        videoList = response.css('.panel-list li')
        next_page = response.css('a[title="下一页"]::attr(href)').extract_first()
        for videodom in videoList:
            item = ScrapyphantomItem()
            item['href'] = videodom.css('a::attr(href)').extract_first()
            item['title'] = videodom.css('a::attr(title)').extract_first()
            item['imgsrc'] = videodom.css('img::attr(src)').extract_first()
            video_page = response.urljoin(item['href'])
            request = scrapy.Request(video_page, self.videoParse)
            request.meta['item'] = item
            yield request
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def videoParse(self, response):
        item = response.meta['item']
        iframedom = response.css('iframe')
        if iframedom is not None:
            iframesrc = response.css('iframe::attr(src)').extract_first()
            iframe_page = response.urljoin(iframesrc)
            item['iframesrc'] = iframe_page
            request = scrapy.Request(iframe_page, self.iframeParse)
            request.meta['item'] = item
            yield request

    def iframeParse(self, response):
        videodom = response.css('video')
        item = response.meta['item']
        if videodom is not None:
            item['m3u8'] = response.css('video::attr(src)').extract_first()
            print(item['m3u8'])
        yield item