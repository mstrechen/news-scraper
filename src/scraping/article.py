from datetime import datetime
from urllib import parse

from elasticsearch import Elasticsearch

class Article:
    def __init__(self, url: str, headline: str, dt: datetime = datetime.now(), tags: list = None):
        self.url = url.strip()
        self.datetime = dt
        self.headline = headline.strip()
        self.img = ""
        self.text = ""
        self.richtext = ""
        self.src_name = ""
        self.tags = [] if tags is None else tags


    def get_source(self):
        return parse.urlparse(self.url).netloc

    def _normilize_time_for_es(self):
        return self.datetime.strftime("%Y-%m-%dT%H:%M:%S")

    def already_exists(self, es: Elasticsearch):
        body = {
            "query" : {
                "match" : {
                    "url" : self.url
                }
            }
        }
        result = es.search(index="news", body=body, request_timeout=1000)["hits"]["total"]
        return result >= 1

    def can_be_updated(self, es: Elasticsearch):
        body = {
            "query" : {
                "match" : {
                    "url" : self.url
                }
            }
        }
        res = es.search(index="news", body=body, request_timeout=1000)["hits"]
        if res["total"] >= 1:
            return not bool(res["hits"][0]["_source"]["text"])
        return True

    def make_tags_into_string(self, tags):
        return " ".join(sorted(tags))

    def insert_into_es(self, es: Elasticsearch):
        es.index(index="news", doc_type="article", body={
            "url": self.url,
            "headline": self.headline,
            "datetime": self._normilize_time_for_es(),
            "img": self.img,
            "src_url": self.get_source(),
            "src_name": self.src_name,
            "text": self.text,
            "richtext" : self.richtext,
            "tags": self.make_tags_into_string(self.tags)
        }, request_timeout=1000)

    def update_in_es(self, es: Elasticsearch):
        body = {
            "query" : {
                "match" : {
                    "url" : self.url
                }
            }
        }
        article_id = \
            es.search(index="news", doc_type="article", body=body, request_timeout=1000)["hits"]["hits"][0]["_id"]
        es.index(index="news", doc_type="article", id=article_id, body={
            "url": self.url,
            "headline": self.headline,
            "datetime": self._normilize_time_for_es(),
            "img": self.img,
            "src_url": self.get_source(),
            "src_name": self.src_name,
            "text": self.text,
            "richtext" : self.richtext,
            "tags": self.make_tags_into_string(self.tags)
        }, request_timeout=1000)
