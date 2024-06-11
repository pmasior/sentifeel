import click
import requests


def download_webpage(url, directory, filename):
    with requests.get(url, timeout=10) as response:
        response_size = (
            int(response.headers["content-length"])
            if "content-length" in response.headers
            else 0
        )
        path = directory / filename
        with click.progressbar(
            length=response_size, label="Downloading"
        ) as progressbar:
            with open(path, "wb") as file:
                for chunk in response.iter_content(chunk_size=4096):
                    file.write(chunk)
                    progressbar.update(4096)


if __name__ == "__main__":
    download_lyrics()
