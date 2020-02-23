# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

class NobelImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url, meta={'handle_httpstatus_list': [301]})

    def item_completed(self, results, item, info):
        
        image_path = [x['path'] for ok, x in results if ok]
        if image_path:
            item['bio_image'] = image_paths[0]

        return item

# class NobelWinnersPipeline(object):
#     """ Remove non-person winners """
#     def process_item(self, item, spider):
#         if not item['gender']:
#             raise DropItem(f'No gender for {item['name']}')
#         return item
