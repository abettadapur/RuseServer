import json
from autobahn.twisted.util import sleep
from autobahn.twisted.wamp import ApplicationSession
from twisted.internet.defer import inlineCallbacks
from ruse.music.gmusic.manager import MusicManager



class AppComponent(ApplicationSession):

    def __init__(self, arg):
        self.music_manager = MusicManager()
        super(AppComponent, self).__init__(arg)

    @inlineCallbacks
    def onJoin(self, details):
        print("session ready: " + str(details))

        def search(query):
            results = self.music_manager.search(query)
            return json.dumps(results)

        def get_album(id):
            album = self.music_manager.get_album_details(id)
            return json.dumps(album)

        def get_artist(id):
            artist = self.music_manager.get_artist_details(id)
            return json.dumps(artist)

        def play_song(id):
            self.music_manager.play_song(id)
            self.send_queue()

        def play_album(id):
            self.music_manager.play_album(id)
            self.send_queue()

        def queue_song(id):
            self.music_manager.queue_song(id)
            self.send_queue()

        def queue_album(id):
            self.music_manager.queue_album(id)
            self.send_queue()

        def set_volume(value):
            self.music_manager.volume(value)

        def pause():
            self.music_manager.pause()

        def resume():
            self.music_manager.resume()

        def next():
            self.music_manager.next()

        def prev():
            self.music_manager.prev()

        def delete(id):
            self.music_manager.delete(id)
            self.send_queue()

        def goto(id):
            self.music_manager.go_to(id)

        def flush():
            self.music_manager.flush()

        try:
            yield self.register(search, u'com.ruse.search')
            yield self.register(get_album, u'com.ruse.get_album')
            yield self.register(get_artist, u'com.ruse.get_artist')
            yield self.register(play_song, u'com.ruse.play_song')
            yield self.register(play_album, u'com.ruse.play_album')
            yield self.register(queue_song, u'com.ruse.queue_song')
            yield self.register(queue_album, u'com.ruse.queue_album')
            yield self.register(set_volume, u'com.ruse.set_volume')
            yield self.register(pause, u'com.ruse.pause')
            yield self.register(resume, u'com.ruse.resume')
            yield self.register(next, u'com.ruse.next')
            yield self.register(prev, u'com.ruse.prev')
            yield self.register(delete, u'com.ruse.delete')
            yield self.register(goto, u'com.ruse.goto')
            yield self.register(flush, u'com.ruse.flush')

            print("Registered methods")
            print("Running server")
            print("Starting status loop")

            while True:
                self.publish(u'com.ruse.now_playing', json.dumps(self.music_manager.get_status()))
                yield sleep(1)


        except Exception as e:
            print("Could not register {0}".format(e))

    def send_queue(self):
        queue  = self.music_manager.get_queue()
        self.publish(u'com.ruse.queue', json.dumps(queue))