import scrapy

class ScrapyphantomItem(scrapy.Item):
    href = scrapy.Field()
    title = scrapy.Field()
    imgsrc = scrapy.Field()
    iframesrc = scrapy.Field()
    m3u8 = scrapy.Field()

