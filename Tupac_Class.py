import requests
from bs4 import BeautifulSoup


class TupacSongs:
    def __init__(self):
        self.address = "https://siachenstudios.com/list/best-tupac-songs/"

    def get_tupac_songs(self):
        respond = requests.get(url=self.address)
        website = respond.text
        soup = BeautifulSoup(website, "html.parser")
        df = soup.select(selector="h2 > strong")
        song_list = [tag.getText().split(" – ")[-1].strip() for tag in df]
        return song_list

