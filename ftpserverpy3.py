from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from os.path import expanduser
import os
import socket
from contextlib import closing
from flask import Flask
import requests

def find_free_port():
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(('', 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]
home = expanduser("~")
authorizer = DummyAuthorizer()
if os.path.exists(home+"/sha2y"):
    serverpath= home+"/sha2y"
else:
    os.mkdir(home+"/sha2y")
    serverpath= home+"/sha2y"
authorizer.add_user("user", "12345", serverpath, perm="elradfmw")
authorizer.add_anonymous(serverpath, perm="elradfmw")
handler = FTPHandler
handler.authorizer = authorizer
PORT = 5000 #= int(os.environ.get("PORT", 5000))
server=FTPServer(("127.0.0.1", 5000), handler)
server.serve_forever()
if server:
    send_response(200, message=ok)

app = Flask(__name__)
@app.route("/")
def hello_world():
    print(requests.get('127.0.0.1'))
    return requests.get('127.0.0.1')
app.run()
