from _azure_connector import get_text_analytics_client
from type_defs.text_analyzer.types import (
    TextAnalysisInput,
    RecognizeLinkedEntitiesOutput,
)


def recognize_linked_entities(
    documents: TextAnalysisInput,
) -> RecognizeLinkedEntitiesOutput:
    client = get_text_analytics_client()
    result = client.recognize_linked_entities(documents)
    return result


if __name__ == "__main__":
    pass
