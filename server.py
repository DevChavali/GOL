
from http.server import SimpleHTTPRequestHandler
import socketserver


class handler(SimpleHTTPRequestHandler):
    
    def do_GET(self):
        self.path = 'index.html'
        return SimpleHTTPRequestHandler.do_GET(self)



with socketserver.TCPServer(('192.168.0.29', 9999), handler) as httpd:
    print('this works?')
    httpd.serve_forever()
    httpd.server_close()


