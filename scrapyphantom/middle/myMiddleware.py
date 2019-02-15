from selenium import webdriver
from scrapy.http import HtmlResponse
import time

class JavaScriptMiddleware(object):
    def process_request(self, request, spider):
        if spider.name == "kpd":
            driver = webdriver.PhantomJS("E:\work\python\phantomjs.exe") #指定使用的浏览器
            driver.get(request.url)
            body = driver.page_source
            print("访问"+request.url)
            return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)
        else:
            return None