from eurovision_getter import eurovision_ranking_getter
from intermediate_constants import constants
from io_helper import cacher


def _get_eurovision_rankings():
    eurovision_rankings = {}
    for year in range(2021, 2025):  # TODO: for year in range(2021, 2024):
        ranking_content = eurovision_ranking_getter.get_eurovision_ranking(year)
        eurovision_rankings[str(year)] = ranking_content
    return eurovision_rankings


def get_eurovision_rankings():
    return cacher.cache2(
        _get_eurovision_rankings,
        constants.I3_PLAYLISTS_EUROVISION,
        "eurovisions",
        "json",
        should_read_from_cache=False,
    )()


if __name__ == "__main__":
    pass
