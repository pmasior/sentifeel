import eurovision_ranking_getter
import intermediate_files_handler


def get_eurovision_rankings():
    intermediate_files_handler.make_intermediate_directory("6_rankings")

    eurovision_rankings = {}
    for year in range(2021, 2025):  # TODO: for year in range(2021, 2024):
        ranking_content = eurovision_ranking_getter.get_eurovision_ranking(year)
        eurovision_rankings[year] = ranking_content
    intermediate_files_handler.save_to_intermediate_directory(
        eurovision_rankings, "6_rankings", "eurovison", "json"
    )

    return eurovision_rankings


if __name__ == "__main__":
    pass
