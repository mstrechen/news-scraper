import json

from datetime import datetime

def feed(args : dict):
    tmp = [{}, {}]
    tmp[0]["headline"] = u"На Львівщині порушили провадження щодо районного голови через корупцію"
    tmp[0]["datetime"] = str(datetime(2018, 1, 5, 11, 59))
    tmp[0]["img"] = "https://img.tsn.ua/cached/1533895990/tsn-ec97a3c0a2ace5bfabc1ed73666af320/thumbs/315x210/84/c4/4b48271dd867e71b5db3bbb6ecabc484.jpg" 
    tmp[0]["source"] = "TSN"
    tmp[0]["text"] = "Something"
    tmp[1]["headline"] = u"Спецслужби Росії готують інформаційні провокації проти України (ВІДЕО) "
    tmp[1]["datetime"] = str(datetime(2018, 1, 5, 16, 21))
    tmp[1]["img"] = ""
    tmp[1]["source"] = "UA|TV"
    tmp[1]["text"] = "Something other" 



    return json.dumps(tmp, ensure_ascii=False)

def search(args : dict):
    tmp = [{}, {}]
    tmp[1]["headline"] = u"На Львівщині порушили провадження щодо районного голови через корупцію"
    tmp[1]["datetime"] = str(datetime(2018, 1, 5, 11, 59))
    tmp[1]["img"] = "https://img.tsn.ua/cached/1533895990/tsn-ec97a3c0a2ace5bfabc1ed73666af320/thumbs/315x210/84/c4/4b48271dd867e71b5db3bbb6ecabc484.jpg" 
    tmp[1]["source"] = "TSN"
    tmp[1]["text"] = "Something"
    tmp[0]["headline"] = u"Спецслужби Росії готують інформаційні провокації проти України (ВІДЕО) "
    tmp[0]["datetime"] = str(datetime(2018, 1, 5, 16, 21))
    tmp[0]["img"] = ""
    tmp[0]["source"] = "UA|TV"
    tmp[0]["text"] = "Something other" 
    

    return json.dumps(tmp, ensure_ascii=False)

def get_avaliable_tags(args : dict):
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