from . import _azure_connector
from type_defs.text_translator.types import TranslationInput, TranslationResult


def translate_texts(documents: TranslationInput, to_language: str) -> TranslationResult:
    client = _azure_connector.get_text_translation_client()
    result = client.translate(body=documents, to_language=[to_language])
    return result


if __name__ == "__main__":
    pass
