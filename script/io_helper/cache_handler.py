import datetime
import json
import os
from pathlib import Path

from io_helper import terminal_printer


def _get_current_datetime():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%y%m%d.%H%M%S.%f")


def _get_current_version():
    version_from_env = os.getenv("INTERMEDIATE_VERSION")
    return version_from_env if version_from_env else _get_current_datetime()


def _get_intermediate_path(label):
    return Path.cwd() / "intermediate" / _get_current_version() / label


def _get_intermediate_file_path(label, filestem, file_extension):
    return _get_intermediate_path(label) / f"{filestem}.{file_extension}"


def make_intermediate_directory(label):
    path = _get_intermediate_path(label)
    os.makedirs(path, exist_ok=True)
    return path


def check_existence_of_file(label, filestem, file_extension):
    path = _get_intermediate_file_path(label, filestem, file_extension)
    return path.exists()


def open_from_intermediate_directory(label, filestem, file_extension):
    path = _get_intermediate_file_path(label, filestem, file_extension)
    with open(path, "r", encoding="utf-8") as file:
        if file_extension == "json":
            terminal_printer.verbose_print(f"Opening {path}")
            content = json.load(file)
        else:
            terminal_printer.verbose_print(f"Opening {path}")
            content = file.read()
    return content


def save_to_intermediate_directory(content, label, filestem, file_extension):
    path = _get_intermediate_file_path(label, filestem, file_extension)
    with open(path, "w", encoding="utf-8") as file:
        if file_extension == "json":
            terminal_printer.verbose_print(f"Saving to {path}")
            json.dump(content, file, ensure_ascii=False, indent=4)
        else:
            terminal_printer.verbose_print(f"Saving to {path}")
            file.write(content)
    terminal_printer.verbose_print(f"Finished saving to {path}")
    return path


if __name__ == "__main__":
    pass
