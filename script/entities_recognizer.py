from azure_connector import get_text_analytics_client


def recognize_entities():
    client = get_text_analytics_client()
    result = client.recognize_entities(["I like apples so much"])
    print(result)


if __name__ == "__main__":
    pass
