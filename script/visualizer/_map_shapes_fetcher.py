from zipfile import ZipFile

from intermediate_constants import constants
from io_helper import cacher, cache_handler
from webpage_downloader import file_downloader


def _fetch_and_extract_map_shapes():
    intermediate_label = constants.ID_NATURAL_EARTH
    filestem = "ne_50m_admin_0_countries"
    path = cacher.cache3(
        file_downloader.download_file,
        intermediate_label,
        filestem,
        "zip",
    )(
        f"https://naciscdn.org/naturalearth/50m/cultural/{filestem}.zip",
        intermediate_label,
    )

    intermediate_path = cache_handler.get_intermediate_path(intermediate_label)
    with ZipFile(path, "r") as file:
        file.extract(f"{filestem}.cpg", intermediate_path)
        file.extract(f"{filestem}.cpg", intermediate_path)
        file.extract(f"{filestem}.prj", intermediate_path)
        file.extract(f"{filestem}.shp", intermediate_path)
        file.extract(f"{filestem}.shx", intermediate_path)


if __name__ == "__main__":
    pass
