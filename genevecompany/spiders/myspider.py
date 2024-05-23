import scrapy


class MyspiderSpider(scrapy.Spider):
    name = "myspider"
    # allowed_domains = ["X"]
    def start_requests(self):
        data=["https://www.genevecompany.com/en/115-ring","https://www.genevecompany.com/en/115-ring?p=2","https://www.genevecompany.com/en/115-ring?p=3","https://www.genevecompany.com/en/115-ring?p=4"]
        for url in data:
            yield scrapy.Request(url=url,dont_filter=True,callback=self.parse)

    def parse(self, response):
        hrefs = response.css('.li-display-block a::attr(href)').getall()
        print(len(hrefs))
        for href in hrefs:
            yield scrapy.Request(href, callback=self.detail)

    def detail(self, response):
        data={}
        url=response.url
        manufacturer = response.xpath('//h1[@class="manufacturer"]/text()').get()
        nombreproducto = response.xpath('//h1[@id="nombreproducto"]/text()').get()
        price = response.xpath('//span[@id="our_price_display"]/text()').get()
        img_src = response.xpath('//img[@id="bigpic"]/@src').get()
        data['manufacturer']=manufacturer
        data['nombreproducto']=nombreproducto
        data['price']=price
        data['img_src']=img_src
        data['url']=url
        yield data

        pass
