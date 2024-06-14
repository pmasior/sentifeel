from azure_connector import get_text_analytics_client


def extract_key_phrases():
    client = get_text_analytics_client()
    result = client.extract_key_phrases(["I like apples so much"])
    print(result)


if __name__ == "__main__":
    pass
