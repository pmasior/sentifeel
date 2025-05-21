from _azure_connector import get_text_analytics_client
from type_defs.text_analyzer.types import TextAnalysisInput, AnalyzeSentimentOutput


def analyze_sentiment(documents: TextAnalysisInput) -> AnalyzeSentimentOutput:
    client = get_text_analytics_client()
    result = client.analyze_sentiment(documents)
    return result


if __name__ == "__main__":
    pass
