from _azure_connector import get_text_analytics_client
from type_defs.text_analyzer.types import TextAnalysisInput, ExtractKeyPhrasesOutput


def extract_key_phrases(documents: TextAnalysisInput) -> ExtractKeyPhrasesOutput:
    client = get_text_analytics_client()
    result = client.extract_key_phrases(documents)
    return result


if __name__ == "__main__":
    pass
