import requests
from bs4 import BeautifulSoup


class ImagineDragons:
    def __init__(self):
        self.address = "https://www.billboard.com/music/rock/imagine-dragons-songs-best-hits-list-8462544/"

    def get_imagine_dragon_songs(self):
        respond = requests.get(url=self.address)
        website = respond.text
        soup = BeautifulSoup(website, "html.parser")
        df = soup.select(selector="p strong")
        song_list = []
        for tag in df:
            first = tag.getText().find('“') + 1
            second = tag.getText().find('”')
            song_list.append(tag.getText()[first:second])
        return song_list

