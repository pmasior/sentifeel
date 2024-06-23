from _azure_connector import get_text_analytics_client
from type_defs.text_analyzer.types import TextAnalysisInput, RecognizeEntitiesOutput


def recognize_entities(documents: TextAnalysisInput) -> RecognizeEntitiesOutput:
    client = get_text_analytics_client()
    result = client.recognize_entities(documents)
    return result


if __name__ == "__main__":
    pass
