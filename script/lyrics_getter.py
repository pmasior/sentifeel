from bs4 import BeautifulSoup

import intermediate_files_handler
import lyrics_id_creator
from lyrics_conditional_downloader import download_lyrics_conditionally


def parse_lyrics_from_tekstowo_html(html_content, directory, filestem):
    soup = BeautifulSoup(html_content, "lxml")
    selected_element = soup.select_one(".song-text .inner-text")
    lyrics = selected_element.text
    intermediate_files_handler.save_to_intermediate_directory(
        lyrics, directory, filestem, "txt"
    )
    return lyrics


def get_lyrics(author, title):
    intermediate_files_handler.make_intermediate_directory("9_html_lyrics")
    intermediate_files_handler.make_intermediate_directory("a_lyrics")

    song_id = lyrics_id_creator.convert_author_and_title_to_tekstowo_id(author, title)
    html_content = download_lyrics_conditionally(
        "9_html_lyrics", author, title, song_id
    )
    lyrics = parse_lyrics_from_tekstowo_html(html_content, "a_lyrics", song_id)

    return lyrics


if __name__ == "__main__":
    pass
