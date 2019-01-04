#!/bin/python3

from http.server import BaseHTTPRequestHandler, HTTPServer

from utility.url import parse_path
import utility.url
import search.methods

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def _set_headers_success(self, contentType : str = 'text/html; charset=utf-8'):
        self.send_response(200)
        self.send_header('Content-type', contentType)
        self.end_headers()

    def _set_headers_error(self, errno : int = 404):
        self.send_response(errno)
        self.end_headers()


    def do_GET(self):
        root = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
        filename, fullpath, filetype, args = parse_path(root, self.path)

        if(filetype in utility.url.static_ext_list and os.path.isfile(fullpath)):
            self._set_headers_success(utility.url.static_ext_list.get(filetype))
            with open(fullpath, 'rb') as fh:
                data = fh.read()
                self.wfile.write(data)
        elif(filename in search.methods.avaliable):
            method = search.methods.avaliable.get(filename)
            try:
                res = method(args)
                self._set_headers_success()
                self.wfile.write(bytes(res, "utf8"))
            except Exception:
                print(Exception)
                self._set_headers_error(500)
        else:
            self._set_headers_error()
    
 
def run(PORT):
  print('starting server...')
  server_address = ('127.0.0.1', PORT)
  httpd = HTTPServer(server_address, HTTPRequestHandler)
  print('running server...')
  httpd.serve_forever()
 
if __name__ == "__main__":
    try:
        import os
        PORT = int(os.environ["PORT"])
    except:
        PORT = 8080
    run(PORT)