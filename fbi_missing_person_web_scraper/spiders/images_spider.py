import scrapy


class ImagesSpider(scrapy.Spider):
    name = "images"

    def start_requests(self):
        urls = [
            'https://www.fbi.gov/wanted/kidnap',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'missing-persons-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')