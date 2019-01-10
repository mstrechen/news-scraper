import importlib

__all__ = ["internetua", "uabanker"]

scrapers = {}


def import_all_scrapers():
    for module in __all__:
        mod = importlib.import_module("." + module, package=__package__)
        to_insert = mod.Scraper()
        scrapers[to_insert.get_url()] = to_insert

import_all_scrapers()
