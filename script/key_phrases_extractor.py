from azure_connector import get_text_analytics_client
from type_defs import Documents


def extract_key_phrases(documents: Documents):
    client = get_text_analytics_client()
    result = client.extract_key_phrases(documents)
    return result


if __name__ == "__main__":
    pass
