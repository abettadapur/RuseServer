import json
from flask import Flask, render_template, request, flash, jsonify
from ruse.music.gmusic.manager import MusicManager
from socketio import socketio_manage
import gevent
import logging
from socketio.namespace import BaseNamespace
from socketio.mixins import BroadcastMixin

logging.basicConfig()
app = Flask(__name__)
app.secret_key = "something secret"
app.debug = True

music_manager = MusicManager()

@app.route('/search', methods=["GET"])
def search():
    query = request.args.get('query')
    results = music_manager.search(query)
    return jsonify(**results)

@app.route('/socket.io/<path:remaining>')
def socketio(remaining):
    print "Rem: " + remaining
    socketio_manage(request.environ, {'/ruse': RuseNamespace})
    return app.response_class


class RuseNamespace(BaseNamespace):

    def recv_connect(self):
        print "connecting"
        def sendStatus():
            while True:
                status = music_manager.get_status()
                print "Publishing: " + str(status)
                self.emit("status", json.dumps(status))
                gevent.sleep(1)

        self.spawn(sendStatus)

    def recv_disconnect(self):
        self.kill_local_jobs()

    def on_play(self, args):
        print args
        music_manager.play_song(args)

    def on_queue(self, args):
        music_manager.queue_song(args)

    def on_volume(self, args):
        music_manager.volume(args)

    def on_pause(self, args):
        music_manager.pause()

    def on_resume(self, args):
        music_manager.resume();

    def on_next(self, args):
        music_manager.next()

    def on_prev(self, args):
        music_manager.prev()

    def on_volume(self, args):
        music_manager.volume(args)

    def on_delete(self, args):
        music_manager.delete(args)

    def on_goto(self, args):
        music_manager.go_to(args)



