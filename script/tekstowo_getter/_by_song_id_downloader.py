from webpage_downloader import webpage_downloader


def _download_by_song_id(song_id: str) -> str:
    return webpage_downloader.download_webpage(
        f"https://www.tekstowo.pl/piosenka,{song_id}.html"
    )


if __name__ == "__main__":
    pass
