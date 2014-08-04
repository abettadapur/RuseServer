
from gevent import monkey; monkey.patch_all();
from socketio.server import SocketIOServer
from ruse.etc.config import config

from ruse.transport.flask.app import app

server = SocketIOServer((config.BIND, config.PORT), app, resource="socket.io")

if __name__ == '__main__':
    print 'Running server'
    server.serve_forever()