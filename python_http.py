from http.server import SimpleHTTPRequestHandler, HTTPServer


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('0.0.0.0', 8080)
    httpd = server_class(server_address, handler_class)
    print("launching server...")
    httpd.serve_forever()

if __name__ == "main":
  run()
