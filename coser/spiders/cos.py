# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from ..items import CoserItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CosSpider(CrawlSpider):
    name = 'cos'
    allowed_domains = ['www.aitaotu.com']
    start_urls = ['http://www.aitaotu.com/tag/cosplay.html']

    rules = (
        Rule(LinkExtractor(allow=r'/\D+/\d+.html'), callback='parse_item'),
    )

    # def parse(self, response):
    #     sel = Selector(response)
    #     for link in sel.xpath("//li[@class='Pli masonry-brick']/a/@href"):
    #         links='https://www.aitaotu.com/%s'%link
    #         request = scrapy.Request(links, callback=self.parse_item)
    #         yield request

    def parse_item(self, response):
        photolist = response.xpath("//div[@class='photo']")
        item = CoserItem()
        item['url']=response.url
        item['name'] = photolist.xpath("./div[@id='photos']/h1/text()").extract()
        item['info'] = photolist.xpath("./div[@class='tsmaincont-main-cont-desc']/h3/text()").extract()
        item['image_urls'] = photolist.xpath("./div[@class='big-pic']/div/p/a/img/@src").extract()

        yield item
