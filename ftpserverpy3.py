from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from os.path import expanduser
home = expanduser("~")
authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", home+"/user", perm="elradfmw")
authorizer.add_anonymous(home+"/user", perm="elradfmw")
handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(('localhost'), handler)
server.serve_forever()
