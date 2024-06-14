import entities_recognizer
import linked_entities_recognizer
import pii_entities_recognizer
import key_phrases_extractor
import lyrics_getter
import sentiment_analyzer
import text_analyzer

if __name__ == "__main__":
    # artist_and_title = "Nemo - The Code"
    # url = "https://www.tekstowo.pl/piosenka,nemo,the_code.html"
    # lyrics_getter.get_lyrics(artist_and_title, url)
    sentiment_analyzer.analyze_sentiment()
    key_phrases_extractor.extract_key_phrases()
    entities_recognizer.recognize_entities()
    linked_entities_recognizer.recognize_linked_entities()
    pii_entities_recognizer.recognize_pii_entities()
    print("finish")
    text_analyzer.analyze_text()
