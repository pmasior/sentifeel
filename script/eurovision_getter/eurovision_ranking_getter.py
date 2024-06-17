from eurovision_getter import _eurovision_ranking_downloader, _eurovision_ranking_parser
from io_helper import cacher


def get_eurovision_ranking(year):
    html_content = cacher.cache_or_update(
        _eurovision_ranking_downloader.download_ranking_from_eurovision,
        "_1_eurovision_html",
        year,
        "html",
        "ALLOW_CONNECT_TO_EUROVISIONWORLD_COM",
    )(year)

    ranking = cacher.cache2(
        _eurovision_ranking_parser.parse_ranking_from_eurovision_html,
        "_2_ranking_json",
        year,
        "json",
    )(html_content)

    return ranking


if __name__ == "__main__":
    pass
