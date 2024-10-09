import scrapy


class BooksToscrapeSpider(scrapy.Spider):
    name = "books_toscrape"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        pass
