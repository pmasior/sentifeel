from bs4 import BeautifulSoup

import intermediate_files_handler
import webpage_downloader


def download_lyrics():
    directory = intermediate_files_handler.make_intermediate_directory("1_downloader")
    url = "https://www.tekstowo.pl/piosenka,nemo,the_code.html"
    webpage_downloader.download_webpage(url, directory, "Nemo - The Code.html")


if __name__ == "__main__":
    pass
