from eurovision_getter import _eurovision_ranking_downloader, _eurovision_ranking_parser
from intermediate_constants import constants
from io_helper import cacher
from type_defs.eurovision_getter.types import RankingItem


def get_eurovision_ranking(year: str) -> list[RankingItem]:
    html_content = cacher.cache_or_update(
        _eurovision_ranking_downloader.download_ranking_from_eurovision,
        constants.I1_EUROVISION_HTML,
        year,
        "html",
        "ALLOW_CONNECT_TO_EUROVISIONWORLD_COM",
    )(year)

    ranking = cacher.cache2(
        _eurovision_ranking_parser.parse_ranking_from_eurovision_html,
        constants.I2_PLAYLIST_EUROVISION,
        year,
        "json",
    )(html_content)

    return ranking


if __name__ == "__main__":
    pass
