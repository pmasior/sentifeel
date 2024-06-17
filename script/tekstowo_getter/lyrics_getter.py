import io_helper.cacher as cacher

from . import _lyrics_id_creator
from . import _lyrics_downloader
from . import _lyrics_parser


def get_lyrics(author, title):
    song_id = _lyrics_id_creator.create_lyrics_id(author, title)

    html_content = cacher.cache_or_update(
        _lyrics_downloader.download_lyrics,
        "_3_tekstowo_html",
        song_id,
        "html",
        "ALLOW_CONNECT_TO_TEKSTOWO_PL",
    )(author, title, song_id)

    lyrics = cacher.cache2(
        _lyrics_parser.parse_lyrics_from_tekstowo_html,
        "_4_tekstowo_txt",
        song_id,
        "txt",
    )(html_content)

    return song_id


if __name__ == "__main__":
    pass
