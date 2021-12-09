from http import server
from http.server import HTTPServer,BaseHTTPRequestHandler
from re import finditer
from flask import Flask,Response
from flask import request
from flask import jsonify
from flask.wrappers import Response


class handlerfunc(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content_type","text/html")
        self.end_headers()
        self.wfile.write('hello world')

app = Flask(__name__)
#End point helloworld to stranger
@app.route("/helloworld")
def helloworld():
    return "Hello Stranger"

#Cample splitting
@app.route("/helloworld?name=AlfredENeumann")
def camel_split(split):
    same = finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', split) #it is similar to splitting:
    return [a.group(0) for a in same]


def main():
    PORT = 8080
    server = HTTPServer(('',PORT),handlerfunc)
    print ('server is running on port %s',PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()
    app.run(debug=True)