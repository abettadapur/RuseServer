import json
from flask import Flask, request
from ruse.music.gmusic.manager import MusicManager
from socketio import socketio_manage
import gevent
import logging
from socketio.namespace import BaseNamespace

logging.basicConfig()
app = Flask(__name__)
app.secret_key = "something secret"
app.debug = True

music_manager = MusicManager()

@app.route('/search', methods=["GET"])
def search():
    query = request.args.get('query')
    results = music_manager.search(query)
    return json.dumps(results)

@app.route('/album', methods=["GET"])
def get_album():
    id = request.args.get("id")
    album = music_manager.get_album_details(id)
    return json.dumps(album)

@app.route('/artist', methods=["GET"])
def get_artist():
    id = request.args.get("id")
    artist = music_manager.get_artist_details(id)
    return json.dumps(artist)

@app.route('/stations', methods=["GET"])
def get_stations():
    stations = music_manager.get_radio_stations()
    print stations
    return json.dumps(stations)

@app.route('/stations/create', methods=["GET"])
def create_radio_station():
    name = request.args.get('name')
    id = request.args.get('id')
    station_id = music_manager.create_radio_station(name, id)
    return json.dumps({'station_id': station_id})

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
                #print "Publishing: " + str(status)
                self.emit("status", json.dumps(status))
                gevent.sleep(1)

        self.spawn(sendStatus)

    def recv_disconnect(self):
        self.kill_local_jobs()

    def on_play(self, args):
        print args
        music_manager.play_song(args)

    def on_playalbum(self, args):
        music_manager.play_album(args)

    def on_queue(self, args):
        music_manager.queue_song(args)

    def on_queuealbum(self, args):
        music_manager.queue_album(args)

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

    def on_delete(self, args):
        music_manager.delete(args)

    def on_goto(self, args):
        music_manager.go_to(args)

    def on_flush(self, args):
        music_manager.flush()



