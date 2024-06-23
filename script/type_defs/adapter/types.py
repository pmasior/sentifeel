from typing import Literal, TypedDict

from type_defs.text_analyzer.types import (
    _CategorizedEntity,
    _LinkedEntity,
    _PiiEntity,
    _SentenceSentiment,
    _SentimentConfidenceScores,
)
from type_defs.eurovision_getter.types import RankingItem


class ItemWithLyrics(TypedDict):
    author: str
    country_code: str
    place: str
    song_id: str
    title: str


Playlist = list[RankingItem]
Playlists = dict[str, list[RankingItem]]
PlaylistWithLyrics = list[ItemWithLyrics]
PlaylistsWithLyrics = dict[str, list[ItemWithLyrics]]


class AnalyzeSentimentParsed(TypedDict):
    confidence_scores: _SentimentConfidenceScores
    id: str
    sentences: list[_SentenceSentiment]
    sentiment: Literal["positive", "neutral", "negative", "mixed"]


class RecognizeEntitiesParsed(TypedDict):
    entities: list[_CategorizedEntity]
    id: str


class RecognizeLinkedEntitiesParsed(TypedDict):
    entities: list[_LinkedEntity]
    id: str


class RecognizePiiEntitiesParsed(TypedDict):
    entities: list[_PiiEntity]
    id: str
    redacted_text: str


class ExtractKeyPhrasesParsed(TypedDict):
    id: str
    key_phrases: list[str]


class TextAnalysisParsed(TypedDict, total=False):
    id: str
    sentiment_analysis: AnalyzeSentimentParsed | None
    entities_recognition: RecognizeEntitiesParsed | None
    linked_entities_recognition: RecognizeLinkedEntitiesParsed | None
    pii_entities_recognition: RecognizePiiEntitiesParsed | None
    key_phrases_recognition: ExtractKeyPhrasesParsed | None


class ItemWithAnalysis(TypedDict):
    author: str
    country_code: str
    entities_recognition: RecognizeEntitiesParsed
    key_phrases_recognition: ExtractKeyPhrasesParsed |
    linked_entities_recognition: RecognizeLinkedEntitiesParsed
    id: str
    pii_entities_recognition: RecognizePiiEntitiesParsed
    place: str
    sentiment_analysis: AnalyzeSentimentParsed
    song_id: str
    title: str


PlaylistWithAnalysis = list[ItemWithAnalysis]
PlaylistsWithAnalysis = dict[str, list[ItemWithAnalysis]]
