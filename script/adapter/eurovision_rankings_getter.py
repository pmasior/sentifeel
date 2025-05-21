from eurovision_getter import eurovision_ranking_getter
from intermediate_constants import constants
from io_helper import cacher, env_helper
from type_defs.adapter.types import Playlists


def _get_eurovision_rankings() -> Playlists:
    eurovision_rankings = {}
    start_year = env_helper.get_int_env_variable("EUROVISION_START_YEAR")
    end_year = env_helper.get_int_env_variable("EUROVISION_END_YEAR")
    years_to_ignore = {2020}
    for year in range(start_year, end_year):
        if year in years_to_ignore:
            continue
        ranking_content = eurovision_ranking_getter.get_eurovision_ranking(year)
        eurovision_rankings[str(year)] = ranking_content
    return eurovision_rankings


def get_eurovision_rankings() -> Playlists:
    return cacher.cache2(
        _get_eurovision_rankings,
        constants.I3_PLAYLISTS_EUROVISION,
        "eurovisions",
        "json",
        should_read_from_cache=False,
    )()


if __name__ == "__main__":
    pass
