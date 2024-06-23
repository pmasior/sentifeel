import os


def verbose_print(text: str) -> None:
    if "VERBOSE" in os.environ:
        if os.getenv("VERBOSE").lower() == "true":
            print(f"{Colors.BRIGHT_BLUE}sen: {Colors.RESET} {text}")


class Colors:
    BRIGHT_BLUE = "\033[94m"
    RESET = "\033[0m"


if __name__ == "__main__":
    pass
