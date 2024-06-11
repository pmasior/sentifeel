from bs4 import BeautifulSoup

import intermediate_files_handler
import webpage_downloader


def download_lyrics_from_tekstowo(url, directory, filestem):
    return webpage_downloader.download_webpage(url, directory, f"{filestem}.html")


def parse_lyrics_from_tekstowo_html(html_content_path, directory, filestem):
    with open(html_content_path, "r") as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, "lxml")
    selected_element = soup.select_one(".song-text .inner-text")
    lyrics_path = directory / f"{filestem}.txt"
    with open(lyrics_path, "w") as file:
        file.write(selected_element.text)
    return lyrics_path


def get_lyrics(artist_and_title, url):
    download_directory = intermediate_files_handler.make_intermediate_directory(
        "1_download"
    )
    lyrics_directory = intermediate_files_handler.make_intermediate_directory(
        "2_lyrics"
    )

    html_content_path = download_lyrics_from_tekstowo(
        url, download_directory, artist_and_title
    )
    lyrics_path = parse_lyrics_from_tekstowo_html(
        html_content_path, lyrics_directory, artist_and_title
    )

    return lyrics_path


if __name__ == "__main__":
    pass
