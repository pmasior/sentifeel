from azure_connector import get_text_analytics_client
from type_defs import Documents


def analyze_sentiment(documents: Documents):
    client = get_text_analytics_client()
    result = client.analyze_sentiment(documents)
    return result


if __name__ == "__main__":
    pass
