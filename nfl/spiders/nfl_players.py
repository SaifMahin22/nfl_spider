import scrapy
from ..items import NflItem
import string

class NflPlayersSpider(scrapy.Spider):
    name = 'nfl_players'

    def start_requests(self):
        base_url='https://www.nfl.com/players/active/{}'
        for i in string.ascii_lowercase:
            url=base_url.format(i)
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        all_urls=response.css('.nfl-o-cta--link::attr(href)').extract()
        for url in all_urls:
            yield scrapy.Request(response.urljoin(url), callback=self.starting_requests)

        next_page = response.css('.nfl-o-table-pagination__next::attr(href)').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def starting_requests(self, response):
        base_url= response.url
        stat_url='stats/logs/'
        year='{}/'
        start_year=2011

        y = start_year
        for i in range(11):
            url=base_url+stat_url+year.format(y)
            y=y+1
            yield scrapy.Request(url, callback=self.second_request)

    def second_request(self, response):

        items=NflItem()
        player_name=response.css('.nfl-c-player-header__title::text').get()
        position= response.css('.nfl-c-player-header__position::text').get()
        table_contents = response.css('.nfl-o-roster')

        if table_contents!=[]:
            for content in table_contents:
                rows = content.css('table tbody tr')
                for row in rows:
                    items['table_header'] = content.css('h3::text').get()
                    items['name'] = player_name
                    items['position'] = position
                    items['URL'] = response.url
                    items['log_year'] = response.url.split('/')[-2]

                    ################# Table Contents ###########
                    items['WK'] = row.css('td:nth-child(1)::text').get()
                    items['Game_Date'] = row.css('td:nth-child(2)::text').get()
                    items['OPP'] = row.css('td:nth-child(3)::text').get()
                    items['RESULT'] = row.css('td:nth-child(4)::text').get()
                    items['REC'] = row.css('td:nth-child(5)::text').get()
                    items['YDS'] = row.css('td:nth-child(6)::text').get()
                    items['AVG'] = row.css('td:nth-child(7)::text').get()
                    items['LNG'] = row.css('td:nth-child(8)::text').get()
                    items['TD'] = row.css('td:nth-child(9)::text').get()
                    items['ATT'] = row.css('td:nth-child(10)::text').get()
                    items['YDS1'] = row.css('td:nth-child(11)::text').get()
                    items['AVG1'] = row.css('td:nth-child(12)::text').get()
                    items['LNG1'] = row.css('td:nth-child(13)::text').get()
                    items['TD1'] = row.css('td:nth-child(14)::text').get()
                    items['FUM'] = row.css('td:nth-child(15)::text').get()
                    items['LOS'] = row.css('td:nth-child(16)::text').get()

                    yield items


