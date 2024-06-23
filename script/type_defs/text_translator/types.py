from azure.ai.translation.text.models import InputTextItem, TranslatedTextItem
from typing import TypedDict


class _InputTextItem:
    text: str


TranslationInput = list[str | InputTextItem]


class _DetectedLanguage(TypedDict):
    language: str
    score: float


class _Translation(TypedDict):
    to: str
    text: str


class _TranslatedTextItem(TypedDict):
    detectedLanguage: _DetectedLanguage
    translations: list[_Translation]


TranslationResult = list[TranslatedTextItem]
