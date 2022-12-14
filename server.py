from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = ''
PORT = 8001

class Handler(BaseHTTPRequestHandler):
    def do_hello(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write(bytes(f"<p>Hello <b>{self.path[1:]}</b></p>".encode()))
    def do_GET(self):
        return self.do_hello()

with HTTPServer((HOST, PORT), Handler) as httpd:
    print(f"Running on http://{HOST}:{PORT}")
    httpd.serve_forever()
    httpd.server_close()
