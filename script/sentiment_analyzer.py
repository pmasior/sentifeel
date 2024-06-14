from azure_connector import get_text_analytics_client


def analyze_sentiment():
    client = get_text_analytics_client()
    result = client.analyze_sentiment(["I like apples so much"])
    print(result)


if __name__ == "__main__":
    pass
