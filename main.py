from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from Billboard_Class import HotSongs
from Tupac_Class import TupacSongs
from Rihanna_Class import RihannaSongs
from Dragon_Class import ImagineDragons
from Spotify_Class import SpotifyWorker


WRITE_FONT = ("Helvetica", 12, "bold")
LIGHT_FONT = ("Helvetica", 13, "normal")
HEAD_FONT = ("Helvetica", 15, "bold")
SINGERS = ("Tupac", "Rihanna", "Imagine Dragons", "Dua Lipa", "B.I.G Notorious", "Songs From Past")


class SpotifyApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Spotify Application")
        self.window.geometry("1360x800")
        self.window.state("zoomed")
        # friend classes:
        self.hot_tool = HotSongs()
        self.tupac_tool = TupacSongs()
        self.rihanna_tool = RihannaSongs()
        self.dragon_tool = ImagineDragons()
        # Spotify Variables:
        self.user_id = None
        self.playlist_id = None
        self.available_song_list = []
        self.available_track_codes = []
        # inside variables:
        self.entered_date = StringVar()
        self.playlist_name = StringVar()
        self.chosen_artist = StringVar()

        # interface:
        # ============================= TOMMY FRAME ================================== #
        self.left_frame = Frame(self.window, highlightthickness=2, relief=RIDGE)
        self.left_frame.place(x=5, y=10, width=380, height=650)

        tom_image = Image.open("IMG/tom.png")
        tom_photo = ImageTk.PhotoImage(tom_image)
        self.tom_label = Label(self.left_frame, image=tom_photo)
        self.tom_label.image = tom_photo
        self.tom_label.place(x=5, y=90, width=360, height=540)

        # ============================= ARTUR FRAME ================================== #
        self.right_frame = Frame(self.window, highlightthickness=2, relief=RIDGE)
        self.right_frame.place(x=980, y=10, width=380, height=650)

        art_image = Image.open("IMG/art.png")
        art_photo = ImageTk.PhotoImage(art_image)
        self.art_label = Label(self.right_frame, image=art_photo)
        self.art_label.image = art_photo
        self.art_label.place(x=5, y=90, width=360, height=540)

        # ============================= CENTER FRAME ================================== #
        self.center_frame = Frame(self.window, bd=2, highlightthickness=2, relief=RIDGE)
        self.center_frame.place(x=390, y=10, width=585, height=650)

        # ============================= CENTRAL OBJECTS ================================ #
        self.head_label = Label(self.center_frame, text="Automate Spotify Application", font=HEAD_FONT,
                                justify="center", bd=1, highlightthickness=1, relief=RIDGE)
        self.head_label.place(x=5, y=5, width=565, height=50)

        used_image = Image.open("IMG/spotify.png")
        used_photo = ImageTk.PhotoImage(used_image)
        self.image_label = Label(self.center_frame, image=used_photo)
        self.image_label.image = used_photo
        self.image_label.place(x=90, y=60, width=412, height=125)

        # ============================= ARTISTS SECTION ============================ #
        pac_image = Image.open("IMG/tupac.jpg")
        pac_photo = ImageTk.PhotoImage(pac_image)
        self.tupac_label = Label(self.center_frame, image=pac_photo, bd=1, highlightthickness=1, relief=RIDGE)
        self.tupac_label.image = pac_photo
        self.tupac_label.place(x=10, y=190, width=90, height=120)

        rihanna_image = Image.open("IMG/rihanna.png")
        rihanna_photo = ImageTk.PhotoImage(rihanna_image)
        self.rihanna_label = Label(self.center_frame, image=rihanna_photo, bd=1, highlightthickness=1, relief=RIDGE)
        self.rihanna_label.image = rihanna_photo
        self.rihanna_label.place(x=120, y=190, width=95, height=120)

        dragon_image = Image.open("IMG/imagine.jpg")
        dragon_photo = ImageTk.PhotoImage(dragon_image)
        self.dragon_label = Label(self.center_frame, image=dragon_photo, bd=1, highlightthickness=1, relief=RIDGE)
        self.dragon_label.image = dragon_photo
        self.dragon_label.place(x=233, y=190, width=114, height=120)

        dua_image = Image.open("IMG/dua.jpg")
        dua_photo = ImageTk.PhotoImage(dua_image)
        self.dua_label = Label(self.center_frame, image=dua_photo, bd=1, highlightthickness=1, relief=RIDGE)
        self.dua_label.image = dua_photo
        self.dua_label.place(x=365, y=190, width=87, height=120)

        big_image = Image.open("IMG/big.jpg")
        big_photo = ImageTk.PhotoImage(big_image)
        self.big_label = Label(self.center_frame, image=big_photo, bd=1, highlightthickness=1, relief=RIDGE)
        self.big_label.image = big_photo
        self.big_label.place(x=473, y=190, width=96, height=120)

        # ============================= LEFT SIDE ================================== #
        self.artist_name = Label(self.center_frame, text="Singer Name", font=WRITE_FONT, bd=1,
                                 highlightthickness=1, relief=RIDGE, bg="light cyan")
        self.artist_name.place(x=5, y=320, width=120, height=30)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", foreground="dark green")

        self.artist_box = ttk.Combobox(self.center_frame, font=WRITE_FONT, justify="center",
                                       textvariable=self.chosen_artist)
        self.artist_box["values"] = SINGERS
        self.artist_box.current(0)
        self.artist_box.place(x=130, y=320, width=155, height=30)

        self.date_label = Label(self.center_frame, text="Enter Date", font=WRITE_FONT, bd=1,
                                highlightthickness=1, relief=RIDGE, bg="light cyan")
        self.date_label.place(x=5, y=355, width=120, height=30)

        self.date_entry = Entry(self.center_frame, font=WRITE_FONT, justify="center",
                                textvariable=self.entered_date, fg="dark green")
        self.date_entry.place(x=130, y=355, width=155, height=30)

        self.found_songs_list = Listbox(self.center_frame, font=WRITE_FONT)
        self.found_songs_list.place(x=5, y=390, width=280, height=205)

        self.search_button = Button(self.center_frame, text="Search", font=WRITE_FONT, justify="center",
                                    bg="sea green", fg="white smoke", command=self.search_method)
        self.search_button.place(x=5, y=600, width=133, height=30)

        self.close_button = Button(self.center_frame, text="Close", font=WRITE_FONT, justify="center",
                                   bg="burlywood", command=self.close_method)
        self.close_button.place(x=151, y=600, width=133, height=30)

        # ============================= RIGHT SIDE ================================== #
        self.playlist_label = Label(self.center_frame, text="Playlist Name", font=WRITE_FONT, bd=1,
                                    highlightthickness=1, relief=RIDGE, bg="beige", fg="midnight blue")
        self.playlist_label.place(x=300, y=320, width=120, height=30)

        self.playlist_entry = Entry(self.center_frame, font=WRITE_FONT, justify="center",
                                    textvariable=self.playlist_name, fg="maroon")
        self.playlist_entry.place(x=425, y=320, width=145, height=30)

        self.desc_label = Label(self.center_frame, text="Description", font=WRITE_FONT, bd=1,
                                highlightthickness=1, relief=RIDGE, bg="beige", fg="midnight blue")
        self.desc_label.place(x=300, y=355, width=270, height=30)

        self.desc_text = Text(self.center_frame, font=LIGHT_FONT, fg="maroon")
        self.desc_text.place(x=300, y=390, width=270, height=150)

        self.create_button = Button(self.center_frame, text="Create Playlist", font=WRITE_FONT, justify="center",
                                    bg="coral", command=self.create_playlist_method)
        self.create_button.place(x=300, y=565, width=270, height=30)

        self.add_button = Button(self.center_frame, text="Add Tracks", font=WRITE_FONT, justify="center",
                                 bg="dark slate blue", fg="white smoke", command=self.add_track_method)
        self.add_button.place(x=300, y=600, width=270, height=30)

    # ================================ FUNCTIONALITY ================================== #
    def close_method(self):
        self.window.destroy()

    def search_method(self):
        self.found_songs_list.delete(0, END)

        if self.chosen_artist.get() == "Songs From Past":
            chosen_date = self.entered_date.get()
            self.available_song_list = self.hot_tool.get_songs(chosen_date)
            self.found_songs_list.config(fg="dark olive green")
        elif self.chosen_artist.get() == "Tupac":
            self.available_song_list = self.tupac_tool.get_tupac_songs()
            self.found_songs_list.config(fg="dark slate gray")
        elif self.chosen_artist.get() == "Rihanna":
            self.available_song_list = self.rihanna_tool.get_rihanna_songs()
            self.found_songs_list.config(fg="crimson")
        elif self.chosen_artist.get() == "Imagine Dragons":
            self.available_song_list = self.dragon_tool.get_imagine_dragon_songs()
            self.found_songs_list.config(fg="midnight blue")

        number = 1
        for song in self.available_song_list:
            self.found_songs_list.insert(number, f"{number}) {song}")
            number += 1

    def create_playlist_method(self):
        spotify_tool = SpotifyWorker()
        self.user_id = spotify_tool.generate_token()
        self.playlist_id = spotify_tool.create_playlist(
            remembered_user_id=self.user_id,
            name=self.playlist_name.get(),
            my_description=self.desc_text.get("1.0", END)
        )
        messagebox.showinfo(title="confirm", message="playlist has been created!")

    def add_track_method(self):
        spotipy_hand = SpotifyWorker()
        self.available_track_codes = spotipy_hand.find_track_uris(self.available_song_list)
        spotipy_hand.add_track_to_spotify(
            remembered_playlist_id=self.playlist_id,
            remembered_song_codes=self.available_track_codes
        )
        messagebox.showinfo(title="confirm", message="songs have been added!")


def launch_app():
    app = Tk()
    SpotifyApp(app)
    app.mainloop()


if __name__ == "__main__":
    launch_app()
