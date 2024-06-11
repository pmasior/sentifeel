import datetime
import os
from pathlib import Path


def get_current_datetime():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%y%m%d.%H%M%S.%f")


def get_current_version():
    version_from_env = os.getenv("INTERMEDIATE_VERSION")
    return version_from_env if version_from_env else get_current_datetime()


def make_intermediate_directory(label):
    path = Path.cwd() / "intermediate" / get_current_version() / label
    os.makedirs(path, exist_ok=True)
    return path


if __name__ == "__main__":
    pass
