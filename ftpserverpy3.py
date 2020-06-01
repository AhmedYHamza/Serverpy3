from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from os.path import expanduser
import os
home = expanduser("~")
os.mkdir(home+"/user")
authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", home+"/user", perm="elradfmw")
authorizer.add_anonymous(home+"/user", perm="elradfmw")
handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(("127.0.0.1", 21), handler)
server.serve_forever()
