#nwinners_list_spider.py

import scrapy
import re


BASE_URL = 'http://en.wikipedia.org'


class NWinnerItem(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
    mini_bio = scrapy.Field()
    image_urls = scrapy.Field()
    bio_image = scrapy.Field()
    images = scrapy.Field()


class NWinnerSpiderBio(scrapy.Spider):
    """ Scrapes the Nobel prize biography pages for portrait images and a biographical snippet. """

    name = 'nwinners_minibio'
    allowed_domains = ['en.wikipedia.org']
    start_urls = [
        'http://en.wikipedia.org/wiki/List_of_Nobel_laureates_by_country'
    ]

    def parse(self, response):

        filename = response.url.split('/')[-1]
        h3s = response.xpath('//h3')

        for h3 in h3s:
            country = h3.xpath('span[@class="mw-headline"]/text()').extract()
            if country:
                winners = h3.xpath('following-sibling::ol[1]')
                for w in winners.xpath('li'):
                    wdata = {}
                    wdata['link'] = BASE_URL + w.xpath('a/@href').extract()[0]
                    request = scrapy.Request(
                            wdata['link'],
                            callback=self.get_mini_bio,
                            dont_filter=True)
                    request.meta['item'] = NWinnerItem(**wdata)
                    yield request

    def get_mini_bio(self, response):
        """ Get the winner's bio-text and photo. """

        BASE_URL_ESCAPE = 'http:\/\/en.wikipedia.org'
        item = response.meta['item']
        item['image_urls'] = []
        img_src = response.xpath(
                '//table[contains(@class, "infobox")]//img/@src')
        if img_src:
            item['image_urls'] = ['http:' + img_src[0].extract()]
        mini_bio = ''
        paras = response.xpath(
                '//*[@id="mw-content-text"]/div/p[text() or' \
                        'nomalize-space(.)=""]').extract()

        for p in paras:
            if p == '<p></p>':
                break
            mini_bio += p

        mini_bio = mini_bio.replace('href="/wiki', f'href={BASE_URL}/wiki')
        mini_bio = mini_bio.replace('href="#', item['link'] + '#')
        item['mini_bio'] = mini_bio
        yield item


