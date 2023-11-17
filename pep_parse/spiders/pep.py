import re

import scrapy

from ..items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_links = response.css(
            'section#numerical-index tbody tr td:nth-child(2) a::attr(href)')
        for pep_link in pep_links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('section#pep-content h1::text').get().strip()
        match = re.search(r'PEP\s*(\d+)\s*\W\s*(.*)$', title)
        number = match.group(1)
        name = match.group(2)
        table_row_names = response.css(
            'section#pep-content dl dt::text').getall()
        status_row_number = table_row_names.index('Status') + 1
        status = response.css(
            f'section#pep-content dl dd:nth-of-type({status_row_number}) '
            'abbr::text'
        ).get().strip()
        yield PepParseItem(
            number=number,
            name=name,
            status=status
        )
