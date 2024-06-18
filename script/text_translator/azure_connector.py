from azure.core.credentials import AzureKeyCredential
from azure.ai.translation.text import TextTranslationClient

from io_helper import env_helper


def _get_azure_endpoint():
    return env_helper.get_env_variable_or_throw("AZURE_TRANSLATOR_ENDPOINT")


def _get_azure_key():
    return AzureKeyCredential(
        env_helper.get_env_variable_or_throw("AZURE_TRANSLATOR_KEY")
    )


def _get_azure_region():
    return env_helper.get_env_variable_or_throw("AZURE_TRANSLATOR_REGION")


def get_text_translation_client():
    return TextTranslationClient(
        endpoint=_get_azure_endpoint(),
        credential=_get_azure_key(),
        region=_get_azure_region(),
    )


if __name__ == "__main__":
    pass
