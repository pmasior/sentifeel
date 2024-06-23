from bs4 import BeautifulSoup


def parse_lyrics_from_tekstowo_html(html_content: str) -> str:
    soup = BeautifulSoup(html_content, "lxml")
    selected_element = soup.select_one(".song-text .inner-text")
    lyrics = selected_element.text
    return lyrics


if __name__ == "__main__":
    pass
