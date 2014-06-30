import requests
from subprocess import Popen
import atexit

class VlcManager(object):

    def __init__(self):
        self.url = 'http://localhost:8080/requests/status.json'
        self.vlc = Popen(['vlc', '-Idummy'])

        def kill():
            self.vlc.kill()

        atexit.register(kill)



    def playSong(self, url):
        payload = {'command': 'in_play', 'input': url}
        requests.get(self.url, params=payload, auth=('', 'ruse'))

    def queueSong(self, url):
        payload = {'command': 'in_enqueue', 'input': url}
        requests.get(self.url, params=payload, auth=('', 'ruse'))

    def next(self):
        payload = {'command': 'pl_next'}
        requests.get(self.url, params=payload, auth=('', 'ruse'))

    def prev(self):
        payload = {'command': 'pl_previous'}
        requests.get(self.url, params=payload, auth=('', 'ruse'))

    def pause(self):
        payload = {'command': 'pl_pause'}
        requests.get(self.url, params=payload, auth=('', 'ruse'))

    def resume(self):
        payload = {'command': 'pl_play'}
        requests.get(self.url, params=payload, auth=('', 'ruse'))

    def setVolume(self, val):
        val = (val/100.0)*512;
        payload = {'command': 'volume', 'val': val}
        requests.get(self.url, params=payload, auth=('', 'ruse'))

    def delete(self, id):
        payload = {'command': 'pl_delete', 'id': id}
        requests.get(self.url, params=payload, auth=('', 'ruse'))

    def go_to(self, id):
        payload = {'command': 'pl_play', 'id': id}
        requests.get(self.url, params=payload, auth=('', 'ruse'))

    def get_status(self):
        player_status = requests.get(self.url, auth=('', 'ruse')).json()
        queue_status = requests.get('http://localhost:8080/requests/playlist.json', auth=('', 'ruse')).json()
        status = {k: player_status[k] for k in ('volume', 'length', 'state', 'time')}
        status['playing'] = status['state'] == "playing"
        status['volume'] = int((status['volume'] / 512.0) * 100)
        del status['state']
        songs = queue_status['children'][0]['children']
        status['queue'] = songs
        return status

