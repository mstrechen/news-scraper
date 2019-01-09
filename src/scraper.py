
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

    logging.basicConfig(level=logging.DEBUG)

def start_scraping():
    print("Adding scripts...")
    