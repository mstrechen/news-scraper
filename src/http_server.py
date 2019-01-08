"""
    Manages all things that http server should manage
"""

import os

from http.server import BaseHTTPRequestHandler, HTTPServer

from utility.url import parse_path
import utility.url
import search.methods

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def _set_headers_success(self, content_type: str = 'text/html; charset=utf-8'):
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def _set_headers_error(self, errno: int = 404):
        self.send_response(errno)
        self.end_headers()


    def do_GET(self):
        root = os.path.join(os.getcwd(), 'static')
        filename, fullpath, filetype, args = parse_path(root, self.path)

        if(filetype in utility.url.static_ext_list and os.path.isfile(fullpath)):
            self._set_headers_success(utility.url.static_ext_list.get(filetype))
            with open(fullpath, 'rb') as data_stream:
                data = data_stream.read()
                self.wfile.write(data)
        elif filename in search.methods.avaliable:
            method = search.methods.avaliable.get(filename)
            try:
                res = method(args)
                self._set_headers_success()
                self.wfile.write(bytes(res, "utf8"))
            except Exception as e:
                print("Something went wrong", e)
                self._set_headers_error(500)
        else:
            self._set_headers_error()

def run_http_server(port):
    print('starting server...')
    server_address = ('127.0.0.1', port)
    httpd = HTTPServer(server_address, HTTPRequestHandler)
    print('running server...')
    httpd.serve_forever()
