#import urlparse
import scrapy
from scrapy.loader import ItemLoader
from npc.items import NpcItem

from scrapy.http import Request

class pwc_tax(scrapy.Spider):
    name = "npc"

    allowed_domains = ["www.privacy.gov.ph"]
    start_urls = ["https://www.privacy.gov.ph/data-privacy-act-primer/",
    "https://www.privacy.gov.ph/advisories/",
    "https://www.privacy.gov.ph/advisory-opinions/",
    "https://www.privacy.gov.ph/commission-issued-orders/"
    ]

    def parse(self, response):
        for link in response.xpath("//a[contains(@href, 'pdf')]"):
            loader = ItemLoader(item=NpcItem(),selector= link)
            base_url = link.xpath('.//@href').extract_first()
            final_url = response.urljoin(base_url)
            
            loader.add_value('file_urls',final_url)
            yield loader.load_item()


