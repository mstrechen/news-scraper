'use strict';


var LOAD_NEWS_LIMIT = 30
var NEWS_LISTED = 0
var TAGS = {}


function getJsonFromUrl() {
    var url = location.search;
    var query = url.substr(1);
    var result = {};
    if(query.length == 0)
        return result;
    query.split("&").forEach(function(part) {
      var item = part.split("=");
      result[item[0]] = decodeURIComponent(item[1]);
    });
    return result;
}

function encode_args(args){
    var res = ""
    for(var key in args){
        if(res.length > 0)
            res += "&"
        res += encodeURI(key) + "=" + encodeURI(args[key])
    }
    return res
}

function make_request(url, args, callback){
    var xmlHttp = new XMLHttpRequest();
    
    xmlHttp.open("GET", url + "?" + encode_args(args));
    
    xmlHttp.onreadystatechange = function(){
        if(xmlHttp.readyState == 4){
            if(xmlHttp.status == 200){
                callback(JSON.parse(xmlHttp.responseText))
            } else {
                alert("Something went wrong with server!");
            }
        } 
    }
    xmlHttp.send(null)
}


function make_tags_list(){
    document.getElementById("tagpanelul").innerHTML = ""

    make_request("/tags", {}, make_tags)
}

function set_search_key_listener(){
    document.getElementById('query').onkeypress = function(e){
        if (!e) e = window.event;
        var keyCode = e.keyCode || e.which;
        if (keyCode == '13'){
          search_by_query();
          return false;
        }
      }
}

var add_more_news = function(){}


function set_scroll_listener(){
    var element = document.getElementById('newslist');
    element.onscroll = function(e){
        if(element.scrollHeight - element.scrollTop - element.clientHeight < 100){
            add_more_news()
        }
    }
}

document.addEventListener("DOMContentLoaded", () =>{
    set_search_key_listener()
    set_scroll_listener()
    
    var req = getJsonFromUrl()
    make_tags_list()
    if("type" in req){
        if(req["type"] == "feed"){
            make_feed();
        } else 
        if(req["type"] == "search"){
            if("q" in req)
                document.getElementById("query").value = req["q"]
            search_by_query()
        }
        else 
        if(req["type"] == "listofsources"){
            show_list_of_sources()
        }
    } else 
        make_feed()
});

function make_search_query_line(){
    var res = "?type=search&q="
    res += encodeURI(document.getElementById("query").value)
    if(location.search != res)
        location.search = res
}

function make_feed_line(){
    var res = "?type=feed"

    if(location.search != res)
        location.search = res
}

function make_listofsources_line(){
    var res = "?type=listofsources"
    if(location.search != res)
        location.search = res
}



function make_tags(listoftags){
    TAGS = listoftags
    for(var key in listoftags){
        var li = document.createElement("li")
        var label = document.createElement("label")
        var checkbox = document.createElement("input")
        checkbox.type = "checkbox"
        checkbox.id = "tag-" + key
        label.appendChild(checkbox)
        label.innerHTML += listoftags[key]
        li.appendChild(label)
        document.getElementById("tagpanelul").appendChild(li)
    }
}



class Article{
    constructor(headline, date, text, img, url){
        this.headline = headline
        this.date = date
        this.text = text
        this.img = img
        this.url = url
    }
    to_html() {
        var res = document.createElement("div")
        res.className = "article"
        var img = document.createElement("div")
        if(this.img != "")
            img.style = `background-image: url(${this.img})`
        else
            img.style = "background-image: url(/img/noimage.png)"
        img.className = "article-img"
        res.appendChild(img)
        var headline = document.createElement("a")
        headline.innerText = this.headline
        headline.href = this.url
        var text = document.createElement("p")
        text.innerText = this.text
        var artcontent = document.createElement("div")
        artcontent.className = "article-content"
        artcontent.appendChild(headline)
        artcontent.appendChild(text)
        res.appendChild(artcontent)
        return res
    }
}

function get_active_tags(){
    var res = []
    for(var key in TAGS)
        if(document.getElementById("tag-" + key).checked)
            res.push(key)
    
    return res
}

function append_feed(){
    var active_tags = get_active_tags()
    if(active_tags.length == 0)
        make_request("/feed", 
            {
                limit : LOAD_NEWS_LIMIT,
                offset : NEWS_LISTED
            }, 
            make_news)
    else
        make_request("/feed", 
        {
            limit : LOAD_NEWS_LIMIT,
            offset : NEWS_LISTED,
            tags : active_tags
        }, 
        make_news)
}

function make_feed(){
    make_feed_line()
    NEWS_LISTED = 0
    add_more_news = append_feed
    document.getElementById("newslist").innerHTML = ""
    append_feed()
}




function append_news(newslist){
    newslist.forEach((el) => {
        console.log()
        document.getElementById("newslist")
            .appendChild(new Article(el["headline"],
                                     el["datetime"], 
                                     el["text"], 
                                     el["img"],
                                     el["url"]).to_html()
                        )
    })
    NEWS_LISTED += newslist.length
}

function make_news(newslist){
    append_news(newslist)
}

function append_search_results(){
    var query_options = getJsonFromUrl()
    make_request("/search", 
        {
            q : query_options["q"], 
            limit : LOAD_NEWS_LIMIT,
            offset : NEWS_LISTED
        }, 
        make_news)
}

function search_by_query(){
    make_search_query_line()
    NEWS_LISTED = 0
    add_more_news = append_search_results
    document.getElementById("newslist").innerHTML = ""
    append_search_results()
}


function show_list_of_sources(){
    make_listofsources_line()
}

function apply_tags(){
    make_feed()
}