from bs4 import BeautifulSoup

from . import _by_song_id_downloader
from . import _by_searching_downloader


def _check_is_not_found(html_content):
    soup = BeautifulSoup(html_content, "lxml")
    selected_element = soup.select_one(".error404")
    return True if selected_element is None else False


def download_lyrics(author, title, song_id):
    html_content = _by_song_id_downloader._download_by_song_id(song_id)
    if _check_is_not_found(html_content):
        html_content = _by_searching_downloader._download_after_search(author, title)
    return html_content


if __name__ == "__main__":
    pass
