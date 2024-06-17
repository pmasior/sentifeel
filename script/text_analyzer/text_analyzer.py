from . import azure_connector
from type_defs import Documents


def analyze_texts(documents: Documents):
    client = azure_connector.get_text_analytics_client()
    max_documents_per_request = 25
    result = []
    for i in (0, len(documents), max_documents_per_request):
        chunk = documents[i : i + max_documents_per_request]
        if chunk:
            poller = client.begin_analyze_actions(
                chunk, actions=azure_connector.get_multiple_text_analytics_actions()
            )
            poller_result = poller.result()
            for results in poller_result:
                result.append(results)
    return result


if __name__ == "__main__":
    pass
