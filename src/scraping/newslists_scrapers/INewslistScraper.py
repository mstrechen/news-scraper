from abc import ABC, abstractmethod

class INewslistScraper(ABC):
    def __init__(self, limit: int = 100):
        self.current_article = 0
        self.limit = limit

    @abstractmethod
    def get_articles_list(self) -> list:
        pass

    @abstractmethod
    def get_source_url(self) -> str:
        pass

    @abstractmethod
    def get_source_name(self) -> str:
        pass

    @abstractmethod
    def get_tags(self) -> list:
        pass
