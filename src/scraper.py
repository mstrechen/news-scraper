from scraping import newslists

def wait_until_elasticsearch_avaliable():
    from elasticsearch import Elasticsearch
    import time

    es = Elasticsearch()
    print("waiting until elasticsearch health becomes yellow (timeout = 5 mins)")

    import logging
    logging.basicConfig(level=logging.ERROR)

    for _ in range(60*5): # 5 minutes timeout
        if es.ping():
            es.cluster.health(wait_for_status='yellow')
            break
        else:
            time.sleep(1)
    else:
        raise TimeoutError("Elasticsearch failed to start.")

    mapping = {"mappings": {
        "article": {
            "properties": {
                "url" : {"type":  "keyword"},
                "headline" : {"type" : "text"},
                "datetime" : 	{"type" : "date"},
                "img" : 			{"type" : "keyword"},
                "src_url" : 	{"type" : "keyword"},
                "src_name" : 	{"type" : "keyword"},
                "text" : 			{"type" : "text"},
                "richtext" : 	{"enabled" : False},
                "tags" : 			{"type" : "text"}
            }
        }
        }
    }
    es.indices.create(index='news', ignore=400, body=mapping)

    logging.basicConfig(level=logging.DEBUG)


def start_scraping():
    print("adding scripts...")
    newslists.init_newslists_scrapers()
    newslists.init_article_scrapers()
    print("scrapping just started!")
    newslists.process_scraping()
