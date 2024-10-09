from pathlib import Path

import scrapy
from scrapy.http import Response


class BooksToscrapeSpider(scrapy.Spider):
    name = "books_toscrape"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response: Response, **kwargs):
        for book in response.css("h3 > a::attr(href)").getall():
            yield {"link": book}

            next_page = response.css("li.next > a::attr(href)").get()
            if next_page:
                yield response.follow(next_page, callback=self.parse)
