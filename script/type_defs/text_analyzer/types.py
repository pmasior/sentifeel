from typing import Literal, TypedDict
from azure.ai.textanalytics import (
    AnalyzeSentimentResult,
    DocumentError,
    ExtractKeyPhrasesResult,
    MinedOpinion,
    RecognizeEntitiesResult,
    RecognizeLinkedEntitiesResult,
    RecognizePiiEntitiesResult,
    TextDocumentInput,
    TextDocumentStatistics,
    TextAnalyticsWarning,
)


class _TextDocumentInput(TypedDict):
    id: str
    text: str
    language: str


TextAnalysisInput = list[str | TextDocumentInput]


class _SentimentConfidenceScores(TypedDict):
    negative: float
    neutral: float
    positive: float


class _SentenceSentiment(TypedDict):
    confidence_scores: _SentimentConfidenceScores
    length: int
    mined_opinions: MinedOpinion | None
    offset: int
    sentiment: Literal["positive", "neutral", "negative"]
    text: str


class _AnalyzeSentimentResult(TypedDict):
    confidence_scores: _SentimentConfidenceScores
    id: str
    is_error: Literal[False] = False
    kind: Literal["SentimentAnalysis"] = "SentimentAnalysis"
    sentences: list[_SentenceSentiment]
    sentiment: Literal["positive", "neutral", "negative", "mixed"]
    statistics: TextDocumentStatistics | None
    warnings: list[TextAnalyticsWarning]


AnalyzeSentimentOutput = list[AnalyzeSentimentResult | DocumentError]


class _CategorizedEntity(TypedDict):
    category: str
    confidence_score: float
    length: int
    offset: int
    subcategory: str | None
    text: str


class _RecognizeEntitiesResult(TypedDict):
    entities: list[_CategorizedEntity]
    id: str
    is_error: Literal[False] = False
    kind: Literal["EntityRecognition"] = "EntityRecognition"
    statistics: TextDocumentStatistics | None
    warnings: list[TextAnalyticsWarning]


RecognizeEntitiesOutput = list[RecognizeEntitiesResult | DocumentError]


class _LinkedEntityMatch(TypedDict):
    confidence_score: float
    length: int
    offset: int
    text: str


class _LinkedEntity(TypedDict):
    bing_entity_search_api_id: str | None
    data_source: str
    data_source_entity_id: str | None
    language: str
    matches: list[_LinkedEntityMatch]
    name: str
    url: str


class _RecognizeLinkedEntitiesResult(TypedDict):
    entities: list[_LinkedEntity]
    id: str
    is_error: Literal[False] = False
    kind: Literal["EntityLinking"] = "EntityLinking"
    statistics: TextDocumentStatistics | None
    warnings: list[TextAnalyticsWarning]


RecognizeLinkedEntitiesOutput = list[RecognizeLinkedEntitiesResult | DocumentError]


class _PiiEntity(TypedDict):
    category: str
    confidence_score: float
    length: int
    offset: int
    subcategory: str | None
    text: str


class _RecognizePiiEntitiesResult(TypedDict):
    entities: list[_PiiEntity]
    id: str
    is_error: Literal[False] = False
    kind: Literal["PiiEntityRecognition"] = "PiiEntityRecognition"
    redacted_text: str
    statistics: TextDocumentStatistics | None
    warnings: list[TextAnalyticsWarning]


RecognizePiiEntitiesOutput = list[RecognizePiiEntitiesResult | DocumentError]


class _ExtractKeyPhrasesResult(TypedDict):
    id: str
    is_error: Literal[False] = False
    key_phrases: list[str]
    kind: Literal["KeyPhraseExtraction"] = "KeyPhraseExtraction"
    statistics: TextDocumentStatistics | None
    warnings: list[TextAnalyticsWarning]


ExtractKeyPhrasesOutput = list[ExtractKeyPhrasesResult | DocumentError]

PossibleAnalyzeTextsOutputs = (
    AnalyzeSentimentResult
    | RecognizeEntitiesResult
    | RecognizeLinkedEntitiesResult
    | RecognizePiiEntitiesResult
    | ExtractKeyPhrasesResult
    | DocumentError
)

AnalyzeTextsOutput = list[list[PossibleAnalyzeTextsOutputs]]
