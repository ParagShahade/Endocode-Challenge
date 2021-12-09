from http import server
from http.server import HTTPServer,BaseHTTPRequestHandler

class handlerfunc(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content_type","text/html")
        self.end_headers()
        self.wfile.write('hello world')
def main():
    PORT = 8080
    server = HTTPServer(('',PORT),handlerfunc)
    print ('server is running on port %s',PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()

