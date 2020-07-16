import scrapy
from MoviesInfoSpider.items import MoviesinfospiderItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
       # 1.提取当前页面的信息
       # 先分组，后提取
       dd_list = response.xpath('//dd')
       for dd in dd_list:
            item = MoviesinfospiderItem()

            item['电影'] = dd.xpath('.//div[@class="movie-hover-info"]/div[1]/span/text()').extract_first().strip()
            item['类型'] = dd.xpath('.//div[@class="movie-hover-info"]/div[2]/text()[2]').extract_first().strip()
            item['上映时间'] = dd.xpath('.//div[@class="movie-hover-info"]/div[4]/text()[2]').extract_first().strip()
            yield item