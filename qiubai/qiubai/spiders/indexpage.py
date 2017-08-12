import scrapy


class QiuBaiSpider(scrapy.Spider):
    name = "qiubai"
    start_urls = [
        "https: // www.qiushibaike.com /",
    ]

    def parse(self, response):
        print response.xpath('//div[@class="content"]').extract()
