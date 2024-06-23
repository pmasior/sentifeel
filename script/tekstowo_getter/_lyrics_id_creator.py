import re


def _convert_string_to_tekstowo_format(string: str) -> str:
    string_after_step1 = string.lower()
    string_after_step2 = re.sub(
        "[\u200b-\u200f\u202a-\u202e\u2060\ufeff]", "", string_after_step1
    )
    string_after_step3 = string_after_step2.replace("&", "")
    string_after_step4 = re.sub(r"[^a-z0-9]", "_", string_after_step3)
    return string_after_step4


def create_lyrics_id(author: str, title: str) -> str:
    converted_author = _convert_string_to_tekstowo_format(author)
    converted_title = _convert_string_to_tekstowo_format(title)
    return f"{converted_author},{converted_title}"


if __name__ == "__main__":
    pass
