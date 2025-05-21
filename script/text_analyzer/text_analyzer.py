from azure.core.paging import ItemPaged

from io_helper import terminal_printer
from type_defs.text_analyzer.types import (
    AnalyzeTextsOutput,
    PossibleAnalyzeTextsOutputs,
    TextAnalysisInput,
)
from . import _azure_connector


def analyze_texts(
    documents: TextAnalysisInput,
) -> AnalyzeTextsOutput:
    client = _azure_connector.get_text_analytics_client()
    max_documents_per_request = 25
    result = []
    for i in range(0, len(documents), max_documents_per_request):
        chunk = documents[i : i + max_documents_per_request]
        if chunk:
            terminal_printer.verbose_print(f"Send chunk {str(chunk)[:100]}")
            poller = client.begin_analyze_actions(
                chunk, actions=_azure_connector.get_multiple_text_analytics_actions()
            )
            terminal_printer.verbose_print(
                f"Finished receiving chunk {str(chunk)[:100]}"
            )
            poller_result: ItemPaged[list[PossibleAnalyzeTextsOutputs]] = (
                poller.result()
            )
            for results in poller_result:
                result.append(results)
    return result


if __name__ == "__main__":
    pass
