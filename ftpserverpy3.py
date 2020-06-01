from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", "C:/Server/user", perm="elradfmw")
authorizer.add_anonymous("C:/Server/user", perm="elradfmw")
handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(('localhost'), handler)
server.serve_forever()
