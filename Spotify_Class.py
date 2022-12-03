import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import os


class SpotifyWorker:
    def __init__(self):
        self.my_username = "chincho"
        self.my_token = SpotifyOAuth(
            client_id=os.environ.get("CLIENT_ID"),
            client_secret=os.environ.get("CLIENT_SECRET"),
            redirect_uri=os.environ.get("REDIRECT_URI"),
            scope="playlist-modify-private",
            show_dialog=True,
            cache_path="token.json"
        )
        self.spotipy_object = spotipy.Spotify(auth_manager=self.my_token)

    def active_token_code(self):
        with open("token.json", "r") as docs:
            output = json.load(docs)
            docs.close()
        return output["access_token"]

    def generate_token(self):
        user_id = self.spotipy_object.current_user()["id"]
        return user_id

    def create_playlist(self, remembered_user_id, name, my_description):
        playlist = self.spotipy_object.user_playlist_create(
            user=remembered_user_id,
            name=name,
            public=False,
            description=my_description
        )
        playlist_id = playlist["id"]
        return playlist_id

    def find_track_uris(self, song_list):
        song_codes = []
        for item in song_list:
            try:
                found_track_uri = self.spotipy_object.search(q=item)
                song_codes.append(found_track_uri["tracks"]["items"][0]["uri"])
            except IndexError:
                pass
        return song_codes

    def add_track_to_spotify(self, remembered_playlist_id, remembered_song_codes):
        self.spotipy_object.playlist_add_items(playlist_id=remembered_playlist_id, items=remembered_song_codes)
        return True

