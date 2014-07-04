from ruse.aural.vlc.manager import VlcManager

class MusicQueue(object):
    def __init__(self):
        self.queue = []
        self.current_index = -1
        self.current_state = "stopped"
        self.vlc = VlcManager()

    def play_song(self, song):
        self.queue.append(song)


    def queue_song(self, song):
        self.queue.append(song)

    def next(self):
        pass

    def prev(self):
        pass

    def pause(self):
        pass
