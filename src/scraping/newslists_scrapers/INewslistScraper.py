from abc import ABC, abstractmethod
from queue import Queue

class INewslistScraper(ABC):
    def __init__(self, limit: int = 100):
        self.current_article = 0
        self.limit = limit

    @abstractmethod
    def push_articles_list(self, queue: Queue):
        pass
