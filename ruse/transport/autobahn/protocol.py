import datetime

import six
from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.util import sleep
from autobahn.twisted import wamp
from ruse.music.gmusic.manager import MusicManager


class RuseProtocol(wamp.ApplicationSession):
    """
    Application code goes here. This is an example component that provides
    a simple procedure which can be called remotely from any WAMP peer.
    It also publishes an event every second to some topic.
    """

    def __init__(self):
        wamp.ApplicationSession.__init__(self)
        self.music_manager = MusicManager()


    @inlineCallbacks
    def onJoin(self, details):

        def play_song(id):
            self.music_manager.play_song(id)

        def queue_song(id):
            self.music_manager.queue_song(id)

        def search(query):
            self.music_manager.search(query)

        def next():
            self.music_manager.next()

        def prev():
            self.music_manager.prev()

        def pause():
            self.music_manager.pause()

        def resume():
            self.music_manager.resume()

        def volume(val):
            self.music_manager.volume(val)

        def delete(id):
            self.music_manager.delete(id)

        def go_to(id):
            self.music_manager.go_to(id)

        self.register(play_song, u'com.ruse.play_song')
        self.register(queue_song, u'com.ruse.queue_song')
        self.register(search, u'com.ruse.search')
        self.register(next, u'com.ruse.next')
        self.register(prev, u'com.ruse.prev')
        self.register(pause, u'com.ruse.pause')
        self.register(resume, u'com.ruse.resume')
        self.register(delete, u'com.ruse.delete')
        self.register(go_to, u'com.ruse.goto')

        while True:
            try:
                status = self.music_manager.get_status()
                print 'Publishing '+str(status)
                self.publish(u'com.ruse.status', status)
            except:
                print "VLC NOT UP"

            yield sleep(1)
