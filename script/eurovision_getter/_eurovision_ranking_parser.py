from bs4 import BeautifulSoup
from bs4.element import Tag

from type_defs.eurovision_getter.types import RankingItem


def _convert_html_row_to_ranking_object(row: Tag) -> RankingItem:
    place = row.select_one("b").text
    country_code = row["id"][-2:]
    title = row.select("td")[2].select_one("a").contents[0].strip()
    author = row.select("td")[2].select_one("span").text
    return {
        "place": place,
        "country_code": country_code,
        "title": title,
        "author": author,
    }


def parse_ranking_from_eurovision_html(html_content: str) -> list[RankingItem]:
    soup = BeautifulSoup(html_content, "lxml")
    table_body_element = soup.select_one(".v_table tbody")
    ranking = []
    for row in table_body_element.select("tr"):
        ranking_object = _convert_html_row_to_ranking_object(row)
        ranking.append(ranking_object)
    return ranking


if __name__ == "__main__":
    pass
