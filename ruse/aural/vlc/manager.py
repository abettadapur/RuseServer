import requests
import vlc

class VlcManager(object):

    def __init__(self):
        self.instance = vlc.Instance("--sub-source marq")
        self.player = self.instance.media_player_new()

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

    def vlc_stop(self):
        self.player.stop()

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


