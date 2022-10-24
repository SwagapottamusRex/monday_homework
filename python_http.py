# from http.server import BaseHTTPRequestHandler, HTTPServer


# def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
#     server_address = ('', 8080)
#     httpd = server_class(server_address, handler_class)
#     httpd.serve_forever()

import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
