from .INewslistScraper import INewslistScraper

class Scraper(INewslistScraper):
    def __init__(self, limit: int = 100):
        INewslistScraper.__init__(self, limit)

    def get_articles_list(self) -> list:
        return []


    def get_source_url(self) -> str:
        return ""

    def get_source_name(self) -> str:
        return ""

    def get_tags(self) -> list:
        return []
