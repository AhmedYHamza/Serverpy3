from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from os.path import expanduser
import os
import socket
from contextlib import closing

def find_free_port():
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(('', 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]
home = expanduser("~")
os.mkdir(home+"/user")
authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", home+"/user", perm="elradfmw")
authorizer.add_anonymous(home+"/user", perm="elradfmw")
handler = FTPHandler
handler.authorizer = authorizer
PORT = int(os.environ.get("PORT", 5000))
server=FTPServer(("127.0.0.1", PORT), handler)
server.serve_forever()
