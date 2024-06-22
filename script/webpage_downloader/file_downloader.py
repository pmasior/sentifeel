import click
import requests
from email.message import EmailMessage

from io_helper import terminal_printer


def _get_filename_from_content_disposition_header(content_disposition):
    message = EmailMessage()
    message["content-disposition"] = content_disposition
    return message.get_filename()


def _get_download_filename(
    url, destination_filename=None, content_disposition_header=None
):
    if destination_filename is not None:
        return destination_filename
    elif content_disposition_header is not None:
        return _get_filename_from_content_disposition_header(content_disposition_header)
    else:
        return url.split("?")[0].split("/")[-1]


def download_file(url, directory, destination_filename=None):
    with requests.get(url, stream=True, timeout=10) as response:
        file_size = (
            int(response.headers["content-length"])
            if "content-length" in response.headers
            else 0
        )
        content_disposition_header = (
            response.headers["content-disposition"]
            if "content-disposition" in response.headers
            else None
        )
        filename = _get_download_filename(
            response.url, destination_filename, content_disposition_header
        )
        path = directory / filename
        terminal_printer.verbose_print(f"Download {url} to {path}")
        with click.progressbar(length=file_size, label="Downloading") as progressbar:
            with open(path, "wb") as file:
                for chunk in response.iter_content(chunk_size=4096):
                    file.write(chunk)
                    progressbar.update(4096)
    terminal_printer.verbose_print(f"Finished download {url} to {path}")
    return path
