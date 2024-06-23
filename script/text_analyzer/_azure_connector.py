from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import (
    TextAnalyticsClient,
    RecognizeEntitiesAction,
    RecognizeLinkedEntitiesAction,
    RecognizePiiEntitiesAction,
    ExtractKeyPhrasesAction,
    AnalyzeSentimentAction,
)

from io_helper import env_helper


def _get_azure_endpoint():
    return env_helper.get_env_variable_or_throw("AZURE_LANGUAGE_ENDPOINT")


def _get_azure_key():
    return AzureKeyCredential(
        env_helper.get_env_variable_or_throw("AZURE_LANGUAGE_KEY")
    )


def get_text_analytics_client():
    return TextAnalyticsClient(
        endpoint=_get_azure_endpoint(), credential=_get_azure_key()
    )


def get_multiple_text_analytics_actions(
    *,
    should_analyze_sentiment=True,
    should_recognize_entities=True,
    should_recognize_linked_entities=True,
    should_recognize_pii_entities=True,
    should_extract_key_phrases=True,
):
    actions = [
        AnalyzeSentimentAction() if should_analyze_sentiment else None,
        RecognizeEntitiesAction() if should_recognize_entities else None,
        RecognizeLinkedEntitiesAction() if should_recognize_linked_entities else None,
        RecognizePiiEntitiesAction() if should_recognize_pii_entities else None,
        ExtractKeyPhrasesAction() if should_extract_key_phrases else None,
    ]
    filteredActions = [a for a in actions if a is not None]
    if not filteredActions:
        raise ValueError(f"No action selected")
    return filteredActions


if __name__ == "__main__":
    pass
