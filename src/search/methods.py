import json
import cgi

from .queries import get_feed, get_searh_results


DEFAULT_OFFSET = 0
DEFAULT_LIMIT = 10

def cut_symbols_of_text(res: list):
    for r in res:
        r["text"] = r["text"][:300]
        r["richtext"] = cgi.escape(r["richtext"][:300])

        

def get_offset_and_limit(args: dict):
    if "offset" in args:
        try:
            offset = int(args["offset"][0])
        except ValueError:
            offset = DEFAULT_OFFSET
    else:
        offset = DEFAULT_OFFSET
    if "limit" in args:
        try:
            limit = int(args["limit"][0])
        except ValueError:
            limit = DEFAULT_OFFSET
    else:
        limit = DEFAULT_LIMIT
    return offset, limit

def get_query(args: dict):
    if "q" in args:
        return args["q"][0]
    return ""

def feed(args: dict):
    offset, limit = get_offset_and_limit(args)
    if not "tags" in args:
        articles = get_feed([], offset=offset, limit=limit)
    else:
        articles = get_feed(args["tags"][0].split(','), offset=offset, limit=limit)
    cut_symbols_of_text(articles)
    return json.dumps(articles, ensure_ascii=False)

def search(args: dict):
    offset, limit = get_offset_and_limit(args)
    query = get_query(args)
    results = get_searh_results(query=query, offset=offset, limit=limit)
    cut_symbols_of_text(results)
    return json.dumps(results, ensure_ascii=False)

def get_avaliable_tags(args: dict):
    get_avaliable_tags.tags = {
        "accidents"     : "Accidents",
        "auto"          : "Automobiles",
        "celebrities"   : "Celebrities life",
        "economics"     : "Economics",
        "fun"           : "Fun things",
        "global"        : "Global (foreign) news",
        "health"        : "Health and helathcare",
        "lady"          : "Ladies stuff",
        "photoreport"   : "Photoreports",
        "politics"      : "Politics",
        "science"       : "Science",
        "society"       : "Society",
        "interesting"   : "Some curious things",
        "sport"         : "Sports",
        "technologies"  : "Technologies",
        "ukraine"       : "Ukrainian news",
        "video"         : "Videos",
    }
    return json.dumps(get_avaliable_tags.tags, ensure_ascii=False)


avaliable = {
    "feed" : feed,
    "search" : search,
    "tags" : get_avaliable_tags
}
