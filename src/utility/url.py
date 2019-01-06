from urllib import parse

def get_extention(filename : str):
    if(filename.find('.') != -1):
        return filename[ filename.find('.') + 1 : ]
    return ''

def parse_path(root : str, path : str):
    path, query = parse.splitquery(path)
    if(path == "/"):
        path = "/index.html"
    query = parse.parse_qs(query, keep_blank_values=True)
    filename = path[path.find('/') + 1 : ]
    return filename, root + path, get_extention(path), query


static_ext_list = {
    "css" : "text/css",
    "js" : "application/javascript",
    "png" : "image/x-icon",
    "jpg" : "image/x-icon",
    "ico" : "image/x-icon",
    "html" : "text/html"
}
