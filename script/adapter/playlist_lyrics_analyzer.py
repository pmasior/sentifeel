from typing import Any

from intermediate_constants import constants
from io_helper import cacher, cache_handler
from text_analyzer import text_analyzer
from type_defs.adapter.types import (
    PlaylistWithAnalysis,
    PlaylistsWithAnalysis,
    PlaylistWithLyrics,
    PlaylistsWithLyrics,
)
from . import _text_analysis_result_parser


def _find_dict_in_array(
    dictionaries_list: list[dict[str, Any]], id_name: str, id_value: str
) -> dict[str, Any]:
    for dictionary in dictionaries_list:
        if dictionary[id_name] == id_value:
            return dictionary


def _get_playlist_analysis(playlist: PlaylistWithLyrics) -> PlaylistWithAnalysis:
    songs_to_analyze = []
    for song in playlist:
        lyrics = cache_handler.open_from_intermediate_directory(
            constants.I5_TEKSTOWO_TXT, song["song_id"], "txt"
        )
        songs_to_analyze.append({"id": song["song_id"], "text": lyrics})
    songs_with_analysis_not_parsed = text_analyzer.analyze_texts(songs_to_analyze)
    songs_with_analysis_parsed = (
        _text_analysis_result_parser.parse_text_analysis_result(
            songs_with_analysis_not_parsed
        )
    )
    songs_with_analysis_and_metadata: PlaylistWithAnalysis = []
    for song in playlist:
        songs_with_analysis_and_metadata.append(
            {
                **_find_dict_in_array(playlist, "song_id", song["song_id"]),
                **_find_dict_in_array(
                    songs_with_analysis_parsed, "id", song["song_id"]
                ),
            }
        )
    return songs_with_analysis_and_metadata


def _get_playlists_analysis(playlists: PlaylistsWithLyrics) -> PlaylistsWithAnalysis:
    playlists_with_analysis = {}
    for playlist in playlists:
        playlists_with_analysis[playlist] = _get_playlist_analysis(playlists[playlist])
    return playlists_with_analysis


def get_playlist_analysis(
    playlist: PlaylistWithLyrics, playlist_name: str
) -> PlaylistWithAnalysis:
    return cacher.cache2(
        _get_playlist_analysis,
        constants.IB_PLAYLIST_WITH_ANALYSIS,
        playlist_name,
        "json",
    )(playlist)


def get_playlists_analysis(
    playlists: PlaylistsWithLyrics, playlists_name: str
) -> PlaylistsWithAnalysis:
    return cacher.cache2(
        _get_playlists_analysis,
        constants.IC_PLAYLISTS_WITH_ANALYSIS,
        playlists_name,
        "json",
        should_read_from_cache=False,
    )(playlists)


if __name__ == "__main__":
    pass
