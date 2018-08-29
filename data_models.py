import math, time
from datetime import datetime

class song:
    def __init__(self, item, added_at=None):
        self.song = item["name"]
        self.artist = item["artists"][0]["name"]
        self.album = item["album"]["name"]
        self.length = int(math.floor(item["duration_ms"] / 1000))
        self.uid = item["id"]
        self.epoch_time = int(time.time())
        self.album_art_url = item["album"]["images"][0]["url"]

        if added_at:
            utc_time = datetime.strptime(added_at, "%Y-%m-%dT%H:%M:%SZ")
            self.saved_time = int((utc_time - datetime(1970, 1, 1)).total_seconds())

    def get_song(self):
        return self.song

    def get_artist(self):
        return self.artist
    
    def get_album(self):
        return self.album

    def get_length(self):
        return self.length
    
    def get_id(self):
        return self.uid

    def get_creation_time(self):
        return self.epoch_time

    def get_saved_time(self):
        return self.saved_time if self.saved_time else None

    def get_album_art_url(self):
        return self.album_art_url

    def set_song(self, new):
        self.song = new

    def set_artist(self, new):
        self.artist = new

    def set_album(self, new):
        self.album = new
    
    def set_length(self, new):
        self.length = new
    
    def set_id(self, new):
        self.uid = new
    
    def set_creation_time(self, new):
        self.epoch_time = int(new)
    
    def set_saved_time(self, new):
        self.saved_time = int(new)

    def set_album_art_url(self, new):
        self.album_art_url = new
