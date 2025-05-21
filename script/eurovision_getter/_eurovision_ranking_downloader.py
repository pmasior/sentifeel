from webpage_downloader import webpage_downloader


def download_ranking_from_eurovision(year: str) -> str:
    return webpage_downloader.download_webpage_in_headless_browser(
        f"https://eurovisionworld.com/eurovision/{year}"
    )


if __name__ == "__main__":
    pass
