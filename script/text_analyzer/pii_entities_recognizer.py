from _azure_connector import get_text_analytics_client
from type_defs import Documents


def recognize_pii_entities(documents: Documents):
    client = get_text_analytics_client()
    result = client.recognize_pii_entities(documents)
    return result


if __name__ == "__main__":
    pass
