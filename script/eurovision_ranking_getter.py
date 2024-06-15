import conditional_downloader
import eurovision_ranking_downloader
import eurovision_ranking_parser
import intermediate_files_handler


def _parse_and_save_ranking_from_eurovision(html_content, year):
    ranking = eurovision_ranking_parser.parse_ranking_from_eurovision_html(html_content)
    intermediate_files_handler.save_to_intermediate_directory(
        ranking, "4_ranking", year, "json"
    )
    return ranking


def get_eurovision_ranking(year):
    intermediate_files_handler.make_intermediate_directory("3_download_ranking")
    intermediate_files_handler.make_intermediate_directory("4_ranking")

    html_content = conditional_downloader.download_conditionally(
        eurovision_ranking_downloader.download_ranking_from_eurovision,
        year,
        "3_download_ranking",
        "ALLOW_CONNECT_TO_EUROVISIONWORLD_COM",
    )
    ranking = _parse_and_save_ranking_from_eurovision(html_content, year)
    return ranking


if __name__ == "__main__":
    pass
