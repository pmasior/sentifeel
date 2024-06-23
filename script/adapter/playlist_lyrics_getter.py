from intermediate_constants import constants
from io_helper import cacher
from tekstowo_getter import lyrics_getter
from type_defs.adapter.types import (
    Playlist,
    Playlists,
    PlaylistWithLyrics,
    PlaylistsWithLyrics,
)


def _get_playlist_lyrics(playlist: Playlist) -> PlaylistWithLyrics:
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


def _get_playlists_lyrics(playlists: Playlists) -> PlaylistsWithLyrics:
    playlists_with_lyrics = {}
    for playlist in playlists:
        playlists_with_lyrics[playlist] = get_playlist_lyrics(playlists[playlist])
    return playlists_with_lyrics


def get_playlist_lyrics(playlist: Playlist, playlist_name: str) -> PlaylistWithLyrics:
    return cacher.cache2(
        _get_playlist_lyrics,
        constants.I6_PLAYLIST_WITH_LYRICS,
        playlist_name,
        "json",
    )(playlist)


def get_playlists_lyrics(
    playlists: Playlists, playlists_name: str
) -> PlaylistsWithLyrics:
    return cacher.cache2(
        _get_playlists_lyrics,
        constants.I7_PLAYLISTS_WITH_LYRICS,
        playlists_name,
        "json",
        should_read_from_cache=False,
    )(playlists)


if __name__ == "__main__":
    pass
