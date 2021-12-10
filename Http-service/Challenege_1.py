from http import server
from http.server import HTTPServer,BaseHTTPRequestHandler
import re
from flask import Flask,Response
from flask import request
from flask.wrappers import Response
import subprocess


app = Flask(__name__)
#End point helloworld to stranger
@app.route("/helloworld")
def helloworld():
    return "Hello Stranger"

#Cample splitting
@app.route("/helloworld?name=AlfredENeumann")
def camel_split(name):
    return ''.join(' ' + cam if cam.isupper() else cam for cam in name) #Split with space

#version
@app.route("/versionz")
def get_git_hash():
    hash_name = subprocess.check_output(['git', 'rev-parse', 'HEAD','describe']) #get value git
    hash_name = str(hash_name, "utf-8").strip()
    return hash_name
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)