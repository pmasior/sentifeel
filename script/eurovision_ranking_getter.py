import json
from bs4 import BeautifulSoup

import intermediate_files_handler
import webpage_downloader


def download_ranking_from_eurovision(year, directory):
    return webpage_downloader.download_webpage_in_headless_browser(
        f"https://eurovisionworld.com/eurovision/{year}", directory, f"{year}.html"
    )


def parse_ranking_from_eurovision_html(html_content_path, directory, filestem):
    with open(html_content_path, "r") as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, "lxml")
    table_body_element = soup.select_one(".v_table tbody")
    data = {}
    data[filestem] = []
    for row in table_body_element.select("tr"):
        place = row.select_one("b").text
        country_code = row["id"][-2:]
        title = row.select("td")[2].select_one("a").contents[0].strip()
        author = row.select("td")[2].select_one("span").text
        data[filestem].append(
            {
                "place": place,
                "country_code": country_code,
                "title": title,
                "author": author,
            }
        )
    ranking_path = directory / f"{filestem}.json"
    with open(ranking_path, "w") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    return ranking_path


def get_ranking(year):
    download_ranking_directory = intermediate_files_handler.make_intermediate_directory(
        "3_download_ranking"
    )
    ranking_directory = intermediate_files_handler.make_intermediate_directory(
        "4_ranking"
    )

    # TODO: Add variable to determine if we should download the ranking or use
    # TODO: existing file and should download missing rankongs or not connect to
    # TODO: website
    # html_content_path = download_ranking_from_eurovision(
    #     year, download_ranking_directory
    # )
    html_content_path = download_ranking_directory / f"{year}.html"
    ranking_path = parse_ranking_from_eurovision_html(
        html_content_path, ranking_directory, year
    )

    return ranking_path


if __name__ == "__main__":
    ranking_path = get_ranking("2024")
    # pass
