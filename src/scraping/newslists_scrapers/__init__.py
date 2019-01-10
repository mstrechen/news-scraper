import importlib

__all__ = ["ukrnet", "tsn"]

scrapers = []


def import_all_scrapers():
    for module in __all__:
        mod = importlib.import_module("." + module, package=__package__)
        scrapers.append(mod.Scraper())


import_all_scrapers()
