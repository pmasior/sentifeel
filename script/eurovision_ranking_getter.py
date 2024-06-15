import env_variables_handler
import eurovision_ranking_parser
import intermediate_files_handler
import webpage_downloader


def _download_conditionally(year):
    def _download_and_save_ranking_from_eurovision(year):
        html_content = webpage_downloader.download_webpage_in_headless_browser(
            f"https://eurovisionworld.com/eurovision/{year}"
        )
        intermediate_files_handler.save_to_intermediate_directory(
            html_content, "3_download_ranking", year, "html"
        )
        return html_content

    def _get_ranking_from_intermediate_files(year):
        return intermediate_files_handler.open_from_intermediate_directory(
            "3_download_ranking", year, "html"
        )

    is_allowing_connect = env_variables_handler.get_boolean_env_variable(
        "ALLOW_CONNECT_TO_EUROVISIONWORLD_COM"
    )
    is_downloaded = intermediate_files_handler.check_existence_of_file(
        "3_download_ranking", year, "html"
    )

    if is_downloaded:
        return _get_ranking_from_intermediate_files(year)
    else:
        if is_allowing_connect:
            return _download_and_save_ranking_from_eurovision(year)
        else:
            raise FileNotFoundError(f"Missing data for {year}")


def _parse_and_save_ranking_from_eurovision(html_content, year):
    ranking = eurovision_ranking_parser.parse_ranking_from_eurovision_html(html_content)
    intermediate_files_handler.save_to_intermediate_directory(
        ranking, "4_ranking", year, "json"
    )
    return ranking


def get_eurovision_ranking(year):
    intermediate_files_handler.make_intermediate_directory("3_download_ranking")
    intermediate_files_handler.make_intermediate_directory("4_ranking")

    html_content = _download_conditionally(year)
    ranking = _parse_and_save_ranking_from_eurovision(html_content, year)
    return ranking


if __name__ == "__main__":
    pass
