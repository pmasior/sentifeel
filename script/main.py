import entities_recognizer
import linked_entities_recognizer
import pii_entities_recognizer
import key_phrases_extractor
import lyrics_getter
import sentiment_analyzer
import text_analyzer
import eurovision_rankings_getter
import lyrics_analyzer
import playlists_lyrics_getter

if __name__ == "__main__":
    eurovision_rankings = eurovision_rankings_getter.get_eurovision_rankings()
    playlists_with_lyrics = playlists_lyrics_getter.get_playlists_lyrics(
        eurovision_rankings, "eurovision"
    )
    lyrics_analyzer.get_playlists_analysis(playlists_with_lyrics, "eurovision")

    # lyrics_getter.get_lyrics(
    #     "Alessandra", "Queen of Kings", "alessandra,queen_of_kings"
    # )
    # lyrics_getter.get_lyrics("Alessandra", "Queen of Kings")
    # artist_and_title = "Nemo - The Code"
    # url = "https://www.tekstowo.pl/piosenka,nemo,the_code.html"
    # lyrics_path = lyrics_getter.get_lyrics(artist_and_title, url)

    # with open(lyrics_path, "r") as file:
    #     lyrics_content = file.read()

    # documents = [
    #     {
    #         "id": artist_and_title,
    #         "text": lyrics_content,
    #     },
    # ]
    # print(documents[0]["text"])
    # print("----")
    # analyzed_sentiments = sentiment_analyzer.analyze_sentiment(documents)
    # for r in analyzed_sentiments:
    #     print(r)
    # extracted_key_phrases = key_phrases_extractor.extract_key_phrases(documents)
    # for r in extracted_key_phrases:
    #     print(r)
    # recognized_entities = entities_recognizer.recognize_entities(documents)
    # for r in recognized_entities:
    #     print(r)
    # recognized_linked_entities = linked_entities_recognizer.recognize_linked_entities(
    #     documents
    # )
    # for r in recognized_linked_entities:
    #     print(r)
    # recognized_pii_entities = pii_entities_recognizer.recognize_pii_entities(documents)
    # for r in recognized_pii_entities:
    #     print(r)
    # print("----")
    # analyzed_texts = text_analyzer.analyze_texts(documents)
    # for r in analyzed_texts:    #     print(r)
