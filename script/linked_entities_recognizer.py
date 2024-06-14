from azure_connector import get_text_analytics_client
from type_defs import Documents


def recognize_linked_entities(documents: Documents):
    client = get_text_analytics_client()
    result = client.recognize_linked_entities(documents)
    return result


if __name__ == "__main__":
    pass
