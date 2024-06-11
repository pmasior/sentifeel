import lyrics_getter

if __name__ == "__main__":
    artist_and_title = "Nemo - The Code"
    url = "https://www.tekstowo.pl/piosenka,nemo,the_code.html"
    lyrics_getter.get_lyrics(artist_and_title, url)
