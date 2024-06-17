from io_helper import cacher
from tekstowo_getter import lyrics_getter


def _get_playlist_lyrics(playlist):
    playlist_with_lyrics = []
    for song in playlist:
        song_id = lyrics_getter.get_lyrics(song["author"], song["title"])
        playlist_with_lyrics.append(
            {
                **song,
                "song_id": song_id,
            }
        )
    return playlist_with_lyrics


def _get_playlists_lyrics(playlists):
    playlists_with_lyrics = {}
    for playlist in playlists:
        playlists_with_lyrics[playlist] = _get_playlist_lyrics(playlists[playlist])
    return playlists_with_lyrics


def get_playlist_lyrics(playlist, playlist_name):
    return cacher.cache2(
        _get_playlist_lyrics,
        "_6_playlist_json",
        playlist_name,
        "json",
    )(playlist)


def get_playlists_lyrics(playlists, playlists_name):
    return cacher.cache2(
        _get_playlists_lyrics,
        "_7_playlists_json",
        playlists_name,
        "json",
    )(playlists)


if __name__ == "__main__":
    pass
