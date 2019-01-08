import json

from .queries import get_feed, get_searh_results

DEFAULT_OFFSET = 0
DEFAULT_LIMIT = 10
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
    articles = get_feed(offset=offset, limit=limit)
    return json.dumps(articles, ensure_ascii=False)

def search(args: dict):
    offset, limit = get_offset_and_limit(args)
    query = get_query(args)
    results = get_searh_results(query=query, offset=offset, limit=limit)
    return json.dumps(results, ensure_ascii=False)

def get_avaliable_tags(args: dict):
    tmp = {}
    tmp["tag1"] = "Tag #1"
    tmp["tag2"] = "Tag #2"
    tmp["tag3"] = "Tag #3"
    tmp["tag4"] = "Tag #4"
    return json.dumps(tmp, ensure_ascii=False)


avaliable = {
    "feed" : feed,
    "search" : search,
    "tags" : get_avaliable_tags
}
