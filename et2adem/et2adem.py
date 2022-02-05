from tqdm import tqdm
from playsound import playsound
import threading
import os

_ROOT = os.path.abspath(os.path.dirname(__file__))
class et2adem(tqdm):
    def __init__(self, loop_data, boring=False, mysong=None):
        self.sound = ~boring
        self.custom_song = mysong
        tqdm.__init__(self, loop_data,
                      bar_format='{l_bar}{bar}{r_bar}',
                      ascii='\U0001f4a8\U0001f3c3',
                      ncols=50)

    def __iter__(self):
        if self.sound:
            stop_threads = False
            threading.Thread(target=self.play_song, args=(lambda: stop_threads,), daemon=True).start()
        yield from super().__iter__()
        stop_threads = True
        return

    def play_song(self, stop):
        if self.custom_song is None:
            path = 'et2dm.wav'
        else:
            path = self.custom_song
        while True:
            playsound(os.path.join(_ROOT, 'data', path))
            if stop():
                break