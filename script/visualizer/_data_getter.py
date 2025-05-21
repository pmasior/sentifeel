from intermediate_constants import constants
from io_helper import cache_handler


def _get_data():
    return cache_handler.open_from_intermediate_directory(
        constants.IC_PLAYLISTS_WITH_ANALYSIS, "eurovision", "json"
    )


if __name__ == "__main__":
    pass
