import requests
from bs4 import BeautifulSoup


class HotSongs:
    def __init__(self):
        self.address = "https://www.billboard.com/charts/hot-100"

    def get_songs(self, entered_date):
        respond = requests.get(url=f"{self.address}/{entered_date}/")
        website = respond.text
        soup = BeautifulSoup(website, "html.parser")
        data = soup.select(selector="li h3", class_="c-title")
        songs = [tag.getText().strip() for tag in data]
        return songs[1:11]

