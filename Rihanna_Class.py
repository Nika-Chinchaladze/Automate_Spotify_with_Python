import requests
from bs4 import BeautifulSoup


class RihannaSongs:
    def __init__(self):
        self.address = "https://www.highsnobiety.com/p/rihanna-best-songs/"

    def get_rihanna_songs(self):
        respond = requests.get(url=self.address)
        website = respond.text
        soup = BeautifulSoup(website, "html.parser")
        df = soup.select(selector="h4 span")
        song_list = []
        for tag in df:
            first_occurrence = tag.getText().find('"') + 1
            second_occurrence = tag.getText().find('"', int(first_occurrence) + 1)
            song_list.append(tag.getText()[first_occurrence:second_occurrence])
        for song in song_list:
            if ("1" in song) \
                    or ("2" in song)\
                    or ("3" in song)\
                    or ("4" in song)\
                    or ("5" in song)\
                    or ("6" in song)\
                    or ("7" in song)\
                    or ("8" in song)\
                    or ("9" in song)\
                    or ("&" in song):
                song_list.remove(song)
            else:
                pass
        return song_list

