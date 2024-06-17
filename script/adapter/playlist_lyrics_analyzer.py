from io_helper import cacher, cache_handler
from text_analyzer import text_analyzer
from . import text_analysis_result_parser


def _find_dict_in_array(dictionaries_list, id_name, id_value):
    for dictionary in dictionaries_list:
        if dictionary[id_name] == id_value:
            return dictionary


def _get_playlist_analysis(playlist):
    songs_to_analyze = []
    for song in playlist:
        lyrics = cache_handler.open_from_intermediate_directory(
            "_4_tekstowo_txt", song["song_id"], "txt"
        )
        songs_to_analyze.append({"id": song["song_id"], "text": lyrics})
    songs_with_analysis_not_parsed = text_analyzer.analyze_texts(songs_to_analyze)
    songs_with_analysis_parsed = text_analysis_result_parser.parse_text_analysis_result(
        songs_with_analysis_not_parsed
    )
    songs_with_analysis_and_metadata = []
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


def _get_playlists_analysis(playlists):
    playlists_with_analysis = {}
    for playlist in playlists:
        playlists_with_analysis[playlist] = _get_playlist_analysis(playlists[playlist])
    return playlists_with_analysis


def get_playlist_analysis(playlist, playlist_name):
    return cacher.cache2(
        _get_playlist_analysis,
        "_8_playlistanalysis_json",
        playlist_name,
        "json",
    )(playlist)


def get_playlists_analysis(playlists, playlists_name):
    return cacher.cache2(
        _get_playlists_analysis,
        "_9_playlists_analysis_json",
        playlists_name,
        "json",
    )(playlists)


if __name__ == "__main__":
    pass
