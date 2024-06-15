import json
import re

import eurovision_ranking_getter
import intermediate_files_handler


def _convert_string_to_tekstowo_format(string):
    string_after_step1 = string.lower()
    string_after_step2 = re.sub('[\u200b-\u200f\u202a-\u202e\u2060\ufeff]', '', string_after_step1)
    string_after_step3 = string_after_step2.replace("&", "")
    string_after_step4 = re.sub(r"[^a-z0-9]", "_", string_after_step3)
    return string_after_step4


def convert_author_and_title_to_tekstowo_id(author, title):
    converted_author = _convert_string_to_tekstowo_format(author)
    converted_title = _convert_string_to_tekstowo_format(title)
    return f"{converted_author},{converted_title}"


def create_lyrics_id(ranking_path, directory, filestem):
    with open(ranking_path, "r") as file:
        data = json.load(file)
    for set in data:
        for song in data[set]:
            song["tekstowo_id"] = convert_author_and_title_to_tekstowo_id(
                song["author"], song["title"]
            )
            song["tekstowo_url"] = f'https://www.tekstowo.pl/piosenka,{convert_author_and_title_to_tekstowo_id(
                song["author"], song["title"]
            )}.html'
    lyrics_link_path = directory / f"{filestem}.json"
    with open(lyrics_link_path, "w") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    return lyrics_link_path


if __name__ == "__main__":
    lyrics_link_directory = intermediate_files_handler.make_intermediate_directory(
        "5_lyrics_link"
    )

    year = "2024"
    ranking_path = eurovision_ranking_getter.get_ranking(year)
    lyrics_link_patk = create_lyrics_id(ranking_path, lyrics_link_directory, year)
