from scrapy.spiders import CrawlSpider, Rule
from IndeedSpider.items import IndeedItem
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
import re

class IndeedSpider(CrawlSpider):
	name="indeed"
	allowed_domains = ["indeed.com.sg"]
	start_urls = ["http://www.indeed.com.sg/jobs?q=plm&l=Singapore"]

	rules = (
		Rule(LinkExtractor(allow=(), restrict_xpaths=('//div[@class="pagination"]/a[position()=last()]',)), callback='parse_item', follow=True),
		)

	def parse_item(self, response):
		for quote in response.xpath('//div[contains(@class, "  row  result")]'):
			yield {
			'title': quote.xpath('./h2/a/text()').extract(),
			}