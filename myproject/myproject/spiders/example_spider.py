import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'example_spider'  # Name of the Spider
    start_urls = ['http://quotes.toscrape.com']  # URL to start with

    def parse(self, response):
        # Extracting quotes and authors
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('span small::text').get(),
            }

        # Following the next page link
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
