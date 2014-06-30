from gmusicapi import Mobileclient
import time
from ruse.aural.vlc.manager import VlcManager
import pprint
from ruse.etc.config import config

class MusicManager(object):

    def __init__(self):
        self.playing_songs = {}
        self.recently_searched = {}
        self.api = Mobileclient()
        self.api.login(config.GOOGLE_USERNAME, config.GOOGLE_PASSWORD)
        self.vlc = VlcManager()

    def play_song(self, id):
        print "play"
        url = self.api.get_stream_url(id, config.GOOGLE_STREAMKEY)
        self.playing_songs[url] = self.recently_searched[id]
        self.vlc.playSong(url)

    def queue_song(self, id):
        url = self.api.get_stream_url(id, config.GOOGLE_STREAMKEY)
        self.playing_songs[url] = self.recently_searched[id]
        self.vlc.queueSong(url)

    def next(self):
        print "next"
        self.vlc.next()

    def prev(self):
        print "prev"
        self.vlc.prev()

    def pause(self):
        self.vlc.pause()

    def resume(self):
        self.vlc.resume()

    def volume(self, val):
        self.vlc.setVolume(val)

    def delete(self, id):
        self.vlc.delete(id)

    def go_to(self, id):
        self.vlc.go_to(id)

    def get_status(self):
        status = self.vlc.get_status()
        queue = status['queue']
        patched_queue = []
        for song in queue:
            patched_song = self.playing_songs[song['uri']]

            if 'current' in song:
                status[u'current'] = self.playing_songs[song['uri']]

            patched_song[u'vlcid'] = song['id']
            patched_song[u'current'] = 'current' in song

            patched_queue.append(patched_song)

        status['queue'] = patched_queue
        return status

    def search(self, query):
        results = self.api.search_all_access(query, max_results=50)

        results['artist_hits'] = [artist['artist'] for artist in results['artist_hits']]

        results['album_hits'] = [album['album'] for album in results['album_hits']]
        for album in results['album_hits']:
            album['artistId'] = album['artistId'][0]

        results['song_hits'] = [song['track'] for song in results['song_hits']]
        for song in results['song_hits']:
            song['albumArtRef'] = song['albumArtRef'][0]['url']
            song['artistId'] = song['artistId'][0]
            self.recently_searched[song['nid']] = song

        return results

if __name__ == "__main__":
    manager = MusicManager()
    results = manager.search('1901')
    id = results['song_hits'][0]['nid']
    manager.play_song(id)
    manager.volume(100)

    while True:
        pprinter = pprint.PrettyPrinter(indent=3)
        pprinter.pprint(manager.get_status())
        time.sleep(1)


