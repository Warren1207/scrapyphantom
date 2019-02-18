from selenium import webdriver
from scrapy.http import HtmlResponse
import time

class JavaScriptMiddleware(object):
    def process_request(self, request, spider):
        print(request.meta)
        if request.meta is not None:
            if 'PhantomJS' in request.meta:
                # driver = webdriver.Chrome("D:\\浏览器代理\chromedriver.exe")  # 指定使用的浏览器
                driver = webdriver.PhantomJS("E:\work\python\phantomjs.exe") #指定使用的浏览器
                driver.get(request.url)
                # time.sleep(2)
                body = driver.page_source
                m3u8Url = driver.execute_script("if(window.video){return window.video[0]}else{return null}")
                item = request.meta['item']
                item['m3u8'] = m3u8Url
                print("访问"+request.url)

                return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)
        else:
            return None