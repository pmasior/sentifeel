from . import azure_connector
from type_defs import Documents


def translate_texts(documents: Documents, to_language: str):
    client = azure_connector.get_text_translation_client()
    result = client.translate(body=documents, to_language=[to_language])
    return result


if __name__ == "__main__":
    pass
