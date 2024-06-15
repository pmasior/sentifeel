import env_variables_handler
import intermediate_files_handler


def download_conditionally(download, filename, temp_dir_name, env_variable_name):
    is_allowing_connect = env_variables_handler.get_boolean_env_variable(
        env_variable_name
    )
    is_downloaded = intermediate_files_handler.check_existence_of_file(
        temp_dir_name, filename, "html"
    )

    if is_downloaded:
        return intermediate_files_handler.open_from_intermediate_directory(
            temp_dir_name, filename, "html"
        )
    else:
        if is_allowing_connect:
            html_content = download(filename)
            intermediate_files_handler.save_to_intermediate_directory(
                html_content, temp_dir_name, filename, "html"
            )
            return html_content
        else:
            raise FileNotFoundError(f"Missing data for {filename}")


if __name__ == "__main__":
    pass
