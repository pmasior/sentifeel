from io_helper import cache_handler


def get_data():
    return cache_handler.open_from_intermediate_directory(
        "_9_playlists_analysis_json", "eurovision", "json"
    )
