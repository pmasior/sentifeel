from azure_connector import (
    get_text_analytics_client,
    get_multiple_text_analytics_actions,
)
from type_defs import Documents


def analyze_texts(documents: Documents):
    client = get_text_analytics_client()
    poller = client.begin_analyze_actions(
        documents, actions=get_multiple_text_analytics_actions()
    )
    result = poller.result()
    return result


if __name__ == "__main__":
    pass
