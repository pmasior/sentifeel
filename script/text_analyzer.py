from azure_connector import (
    get_text_analytics_client,
    get_multiple_text_analytics_actions,
)


def analyze_text():
    client = get_text_analytics_client()
    poller = client.begin_analyze_actions(
        ["I like apples so much"], actions=get_multiple_text_analytics_actions()
    )
    result = poller.result()
    # for
    print(list(result))


if __name__ == "__main__":
    pass
