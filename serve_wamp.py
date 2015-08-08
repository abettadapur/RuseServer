from ruse.etc.config import config
from ruse.transport.autobahn.app import AppComponent
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
from flask import Flask
import threading
from ruse.music import gmusic
import json

app = Flask(__name__)

@app.route('/search/<query>')
def search(query):
    results = gmusic.music_manager.search(query)
    return json.dumps(results)

def start_wamp():
    runner = ApplicationRunner(url=u"ws://{url}:{port}/ws".format(url=config.BIND, port=config.PORT), realm=u"realm1")
    runner.run(AppComponent)

#HTTP Workaround for JAWAMPA
def start_flask():
    app.run(host=config.BIND, port=config.PORT+1)


if __name__ == "__main__":
    t2 = threading.Thread(target=start_flask)
    t2.daemon = True
    t2.start()
    runner = ApplicationRunner(url=u"ws://{url}:{port}/ws".format(url=config.BIND, port=config.PORT), realm=u"realm1")
    runner.run(AppComponent)




