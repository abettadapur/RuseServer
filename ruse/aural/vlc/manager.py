import requests
import vlc

class VlcManager(object):

    def __init__(self, finished_callback):
        self.instance = vlc.Instance("--sub-source marq")
        self.player = self.instance.media_player_new()
        self.event_manager = self.player.event_manager()
        self.event_manager.event_attach(vlc.EventType.MediaPlayerEndReached, finished_callback)

    def vlc_play(self, url):
        self.media = self.instance.media_new(url)
        self.player.set_media(self.media)
        self.player.play()

    def vlc_pause(self):
        self.player.set_pause(1)

    def vlc_resume(self):
        self.player.set_pause(0)

    def vlc_volume(self, val):
        self.player.audio_set_volume(val)

    def vlc_status(self):
        status = {
            'volume': self.player.audio_get_volume(),
            'length': int(self.player.get_length()/1000),
            'time': int(self.player.get_time()/1000),
            'playing': self.player.get_state() == vlc.State.Playing,
        }
        status['time'] = 0 if status['time'] == -1 else status['time']
        status['volume'] = 0 if status['volume'] == -1 else status['volume']
        status['length'] = 0 if status['length'] == -1 else status['length']
        return status


    # def playSong(self, url):
    #     payload = {'command': 'in_play', 'input': url}
    #     requests.get(self.url, params=payload, auth=('', 'ruse'))
    #
    # def queueSong(self, url):
    #     payload = {'command': 'in_enqueue', 'input': url}
    #     requests.get(self.url, params=payload, auth=('', 'ruse'))
    #
    # def next(self):
    #     payload = {'command': 'pl_next'}
    #     requests.get(self.url, params=payload, auth=('', 'ruse'))
    #
    # def prev(self):
    #     payload = {'command': 'pl_previous'}
    #     requests.get(self.url, params=payload, auth=('', 'ruse'))
    #
    # def pause(self):
    #     payload = {'command': 'pl_pause'}
    #     requests.get(self.url, params=payload, auth=('', 'ruse'))
    #
    # def resume(self):
    #     payload = {'command': 'pl_play'}
    #     requests.get(self.url, params=payload, auth=('', 'ruse'))
    #
    # def setVolume(self, val):
    #     val = (val/100.0)*512;
    #     payload = {'command': 'volume', 'val': val}
    #     requests.get(self.url, params=payload, auth=('', 'ruse'))
    #
    # def delete(self, id):
    #     payload = {'command': 'pl_delete', 'id': id}
    #     requests.get(self.url, params=payload, auth=('', 'ruse'))
    #
    # def go_to(self, id):
    #     payload = {'command': 'pl_play', 'id': id}
    #     requests.get(self.url, params=payload, auth=('', 'ruse'))
    #
    # def get_status(self):
    #     player_status = requests.get(self.url, auth=('', 'ruse')).json()
    #     queue_status = requests.get('http://localhost:8080/requests/playlist.json', auth=('', 'ruse')).json()
    #     status = {k: player_status[k] for k in ('volume', 'length', 'state', 'time')}
    #     status['playing'] = status['state'] == "playing"
    #     status['volume'] = int((status['volume'] / 512.0) * 100)
    #     del status['state']
    #     songs = queue_status['children'][0]['children']
    #     status['queue'] = songs
    #     return status

