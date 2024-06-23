import requests
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options

from io_helper import terminal_printer


def download_webpage(url: str) -> str:
    with requests.get(url, timeout=10) as response:
        terminal_printer.verbose_print(f"Download {url}")
        webpage_content = response.content.decode("utf-8")
    terminal_printer.verbose_print(f"Finished download {url}")
    return webpage_content


def _get_headless_browser_driver() -> WebDriver:
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(30)
    driver.set_script_timeout(30)
    return driver


def _close_headless_browser_driver(driver: WebDriver) -> None:
    driver.quit()


def download_webpage_in_headless_browser(url: str) -> str:
    driver = _get_headless_browser_driver()
    terminal_printer.verbose_print(f"Open Firefox and download {url}")
    driver.get(url)
    webpage_content = driver.page_source
    terminal_printer.verbose_print(f"Finished download {url}")
    _close_headless_browser_driver(driver)
    return webpage_content


if __name__ == "__main__":
    pass
