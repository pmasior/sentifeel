from azure_connector import (
    get_text_analytics_client,
    get_multiple_text_analytics_actions,
)
import intermediate_files_handler
import text_analyzer

from type_defs import Documents


def get_playlists_analysis(playlists, playlists_name):
    intermediate_files_handler.make_intermediate_directory("b_playlists_with_analysis")

    playlists_with_lyrics = {}
    for playlist in playlists:
        playlists_with_lyrics[playlist] = get_playlist_analysis(
            playlists[playlist], playlist
        )
    intermediate_files_handler.save_to_intermediate_directory(
        playlists_with_lyrics, "b_playlists_with_analysis", playlists_name, "json"
    )

    return playlists_with_lyrics


def find_dict_in_array(dictionaries_list, id_name, id_value):
    for dictionary in dictionaries_list:
        if dictionary[id_name] == id_value:
            return dictionary


def get_playlist_analysis(playlist, playlist_name):
    intermediate_files_handler.make_intermediate_directory("c_playlist_with_analysis")

    songs_to_analyze = []
    for song in playlist:
        lyrics = intermediate_files_handler.open_from_intermediate_directory(
            "a_lyrics", song["song_id"], "txt"
        )
        songs_to_analyze.append({"id": song["song_id"], "text": lyrics})
    songs_with_analysis = text_analyzer.analyze_texts(songs_to_analyze)
    songs_with_analysis_and_metadata = []
    for song in playlist:
        songs_with_analysis_and_metadata.append(
            {
                **find_dict_in_array(playlist, "song_id", song["song_id"]),
                **find_dict_in_array(songs_with_analysis, "id", song["song_id"]),
            }
        )
    intermediate_files_handler.save_to_intermediate_directory(
        songs_with_analysis_and_metadata,
        "c_playlist_with_analysis",
        playlist_name,
        "json",
    )

    return songs_with_analysis_and_metadata


if __name__ == "__main__":
    pass
