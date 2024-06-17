import re
from bs4 import BeautifulSoup
from urllib.parse import quote

from webpage_downloader import webpage_downloader
from . import _by_song_id_downloader


def _download_after_search(author, title):
    def _get_song_id_from_search(html_content):
        soup = BeautifulSoup(html_content, "lxml")
        selected_element = soup.select_one(".content .title")
        if selected_element is not None:
            song_href = selected_element["href"]
            song_id_regex = re.search(r",([a-z0-9_,]+)\.", song_href)
            return song_id_regex.group(1)
        else:
            return None

    search_query = quote(f"{author} - {title}")
    html_content = webpage_downloader.download_webpage(
        f"https://www.tekstowo.pl/szukaj,{search_query}.html"
    )
    song_id = _get_song_id_from_search(html_content)
    if song_id is not None:
        return _by_song_id_downloader._download_by_song_id(song_id)
    else:
        return r"<div class=song-text><div class=inner-text>.</div></div>"


if __name__ == "__main__":
    pass
