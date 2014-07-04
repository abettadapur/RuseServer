from threading import Thread
from gmusicapi import Mobileclient
import time
from ruse.aural.vlc.manager import VlcManager
from ruse.aural.vlc import vlc
import pprint
from ruse.etc.config import config


class MusicManager(object):

    def __init__(self):
        self.playing_songs = {}
        self.recently_searched = {}
        self.api = Mobileclient()
        self.api.login(config.GOOGLE_USERNAME, config.GOOGLE_PASSWORD)
        self.queue = []
        self.current_index = len(self.queue)-1
        self.vlc = VlcManager(self.on_complete)

    def play_song(self, id):
        self.queue_song(id)
        self.current_index = len(self.queue)-1
        self.load_song()

    def queue_song(self, id):
        self.queue.append(self.recently_searched[id])

    def next(self):
        self.current_index += 1
        self.load_song()

    def prev(self):
        self.current_index -= 1
        self.load_song()

    def pause(self):
        self.vlc.vlc_pause()

    def resume(self):
        self.vlc.vlc_resume()

    def volume(self, val):
        self.vlc.vlc_volume(val)

    def delete(self, id):
        del self.queue[id]
        self.load_song()

    def go_to(self, id):
        self.current_index = id
        self.load_song()

    def on_complete(self, *args, **kwargs):
        print "Complete"

    def load_song(self):
        if self.current_index < len(self.queue):
            song = self.queue[self.current_index]
            url = self.api.get_stream_url(song['nid'], config.GOOGLE_STREAMKEY)
            self.vlc.vlc_play(url)



    def get_status(self):
        status = self.vlc.vlc_status()

        if status['state'] == vlc.State.Ended:
            if self.current_index != len(self.queue)-1:
                self.next()

        del status['state']

        status['queue'] = self.queue[:]
        for i in range(len(status['queue'])):
            status['queue'][i]['vlcid'] = i
            if i == self.current_index:
                status['queue'][i]['current'] = True
                status['current'] = status['queue'][i]
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

    def get_album_details(self, id):
        print id
        results = self.api.get_album_info(album_id=id, include_tracks=True)
        for song in results['tracks']:
            song['albumArtRef'] = song['albumArtRef'][0]['url']
            song['artistId'] = song['artistId'][0]
            self.recently_searched[song['nid']] = song
        return results

    def play_album(self, args):
        album = self.get_album_details(args)
        for index in range(len(album['tracks'])):
            song = album['tracks'][index]
            if index == 0:
                self.play_song(song['nid'])
            else:
                self.queue_song(song['nid'])




if __name__ == "__main__":
    manager = MusicManager()
    results = manager.get_album_details('Bfr2onjv7g7tm4rzosewnnwxxyy')
    id = results['tracks'][0]['nid']
    manager.play_song(id)
    manager.volume(100)

    import pprint
    printer = pprint.PrettyPrinter(indent=2)
    while True:
        time.sleep(1)
        printer.pprint(manager.get_status())



