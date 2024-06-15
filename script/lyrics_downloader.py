import re
from bs4 import BeautifulSoup
from urllib.parse import quote

import webpage_downloader


def _download_by_song_id(song_id):
    return webpage_downloader.download_webpage(
        f"https://www.tekstowo.pl/piosenka,{song_id}.html"
    )


def _check_is_not_found(html_content):
    soup = BeautifulSoup(html_content, "lxml")
    selected_element = soup.select_one(".error404")
    return True if selected_element is None else False


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
        return _download_by_song_id(song_id)
    else:
        return r"<div class=song-text><div class=inner-text> </div></div>"


def download_lyrics(author, title, song_id):
    html_content = _download_by_song_id(song_id)
    if _check_is_not_found(html_content):
        html_content = _download_after_search(author, title)
    return html_content


if __name__ == "__main__":
    pass
