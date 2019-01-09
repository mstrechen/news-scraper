#!/bin/python3

import threading

from http_server import run_http_server
from commands_executor import run_commands_executor
from scraper import start_scraping, wait_until_elasticsearch_avaliable


if __name__ == "__main__":
    try:
        import os
        PORT = int(os.environ["PORT"])
    except (ValueError, KeyError):
        PORT = 8080

    wait_until_elasticsearch_avaliable()

    HTTP_THREAD = threading.Thread(target=run_http_server, args=(PORT,))
    HTTP_THREAD.daemon = True
    HTTP_THREAD.start()

    COMMAND_THREAD = threading.Thread(target=run_commands_executor)
    COMMAND_THREAD.daemon = True
    COMMAND_THREAD.start()

    SCRAPING_THREAD = threading.Thread(target=start_scraping)
    SCRAPING_THREAD.daemon = True
    SCRAPING_THREAD.start()
    