import re

import scrapy

from scrapy.loader import ItemLoader
from ..items import CompassItem
from itemloaders.processors import TakeFirst


class CompassSpider(scrapy.Spider):
	name = 'compass'
	start_urls = ['https://www.compass.it/comunicati-stampa.html',
	              'https://www.compass.it/compass-news.html'
	              ]

	def parse(self, response):
		post_links = response.xpath('//div[contains(@class, "content-teaser-news-comunicate")]/a/@href').getall()
		yield from response.follow_all(post_links, self.parse_post)

	def parse_post(self, response):
		title = response.xpath('//h1/text()').get()
		description = response.xpath('(//div[@class="grid-container padding-bottom-50"])[1]//text()[normalize-space()]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		date = response.xpath('//span[@class="category"]//span/text()').get()
		date = date.split(',')[1]


		item = ItemLoader(item=CompassItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
