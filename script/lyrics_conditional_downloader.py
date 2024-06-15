from env_variables_handler import get_boolean_env_variable
from intermediate_files_handler import (
    check_existence_of_file,
    open_from_intermediate_directory,
    save_to_intermediate_directory,
)
from lyrics_downloader import download_lyrics


def download_lyrics_conditionally(temp_dir_name, author, title, song_id):
    is_allowing_connect = get_boolean_env_variable("ALLOW_CONNECT_TO_TEKSTOWO_PL")
    is_downloaded = check_existence_of_file(temp_dir_name, song_id, "html")

    if is_downloaded:
        html_content = open_from_intermediate_directory(temp_dir_name, song_id, "html")
    else:
        if is_allowing_connect:
            html_content = download_lyrics(author, title, song_id)
            save_to_intermediate_directory(html_content, temp_dir_name, song_id, "html")
        else:
            raise FileNotFoundError(f"Missing data for {song_id}")
    return html_content


if __name__ == "__main__":
    pass
