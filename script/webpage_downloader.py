import click
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import terminal_printer


def download_webpage(url, directory, filename):
    with requests.get(url, timeout=10) as response:
        response_size = (
            int(response.headers["content-length"])
            if "content-length" in response.headers
            else 0
        )
        path = directory / filename
        terminal_printer.verbose_print(f"Download {url} to {path}")
        with click.progressbar(
            length=response_size, label="Downloading"
        ) as progressbar:
            with open(path, "wb") as file:
                for chunk in response.iter_content(chunk_size=4096):
                    file.write(chunk)
                    progressbar.update(4096)
    terminal_printer.verbose_print(f"Finished download {url} to {path}")
    return path


def _get_headless_browser_driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(30)
    driver.set_script_timeout(30)
    return driver


def _close_headless_browser_driver(driver):
    driver.quit()


def download_webpage_in_headless_browser(url, directory, filename):
    driver = _get_headless_browser_driver()
    path = directory / filename
    terminal_printer.verbose_print(f"Open Firefox and download {url} to {path}")
    driver.get(url)
    with open(path, "w") as file:
        file.write(driver.page_source)
    terminal_printer.verbose_print(f"Finished download {url} to {path}")
    _close_headless_browser_driver(driver)
    return path


if __name__ == "__main__":
    pass
