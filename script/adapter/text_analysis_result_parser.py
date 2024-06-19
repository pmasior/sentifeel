def parse_text_analysis_result(poller_results):
    result = []
    for poller_result in poller_results:
        action_converted_result = {}
        for action_result in poller_result:
            action_converted_result["id"] = action_result.id
            if action_result.kind == "SentimentAnalysis":
                action_converted_result["sentiment_analysis"] = {
                    "id": action_result.id,
                    "sentiment": action_result.sentiment,
                    "confidence_scores": {
                        "positive": action_result.confidence_scores.positive,
                        "neutral": action_result.confidence_scores.neutral,
                        "negative": action_result.confidence_scores.negative,
                    },
                    "sentences": [
                        {
                            "text": s.text,
                            "sentiment": s.sentiment,
                            "confidence_scores": {
                                "positive": s.confidence_scores.positive,
                                "neutral": s.confidence_scores.neutral,
                                "negative": s.confidence_scores.negative,
                            },
                            "length": s.length,
                            "offset": s.offset,
                        }
                        for s in action_result.sentences
                    ],
                }
            elif action_result.kind == "EntityRecognition":
                action_converted_result["entities_recognition"] = {
                    "id": action_result.id,
                    "entities": [
                        {
                            "category": e.category,
                            "confidence_score": e.confidence_score,
                            "subcategory": e.subcategory,
                            "length": e.length,
                            "offset": e.offset,
                            "text": e.text,
                        }
                        for e in action_result.entities
                    ],
                }
            elif action_result.kind == "EntityLinking":
                action_converted_result["linked_entities_recognition"] = {
                    "id": action_result.id,
                    "entities": [
                        {
                            "data_source": e.data_source,
                            "language": e.language,
                            "recognized": e.data_source_entity_id,
                            "matches": [
                                {
                                    "confidence_score": m.confidence_score,
                                    "length": m.length,
                                    "offset": m.offset,
                                    "text": m.text,
                                }
                                for m in e.matches
                            ],
                            "name": e.name,
                            "url": e.url,
                        }
                        for e in action_result.entities
                    ],
                }
            elif action_result.kind == "PiiEntityRecognition":
                action_converted_result["pii_entities_recognition"] = {
                    "id": action_result.id,
                    "redacted_text": action_result.redacted_text,
                    "entities": [
                        {
                            "text": e.text,
                            "category": e.category,
                            "confidence_score": e.confidence_score,
                            "subcategory": e.subcategory,
                            "length": e.length,
                            "offset": e.offset,
                        }
                        for e in action_result.entities
                    ],
                }
            elif action_result.kind == "KeyPhraseExtraction":
                action_converted_result["key_phrases_recognition"] = {
                    "id": action_result.id,
                    "key_phrases": action_result.key_phrases,
                }
        result.append(action_converted_result)
    return result


if __name__ == "__main__":
    pass
