import intermediate_files_handler
import lyrics_getter
import lyrics_id_creator


def get_playlist_lyrics(playlist, playlist_name):
    intermediate_files_handler.make_intermediate_directory("8_playlist_with_lyrics")

    playlist_with_lyrics = []
    for song in playlist:
        song_id = lyrics_id_creator.convert_author_and_title_to_tekstowo_id(
            song["author"], song["title"]
        )
        lyrics_getter.get_lyrics(song["author"], song["title"])
        playlist_with_lyrics.append(
            {
                **song,
                "song_id": song_id,
            }
        )
    intermediate_files_handler.save_to_intermediate_directory(
        playlist_with_lyrics, "8_playlist_with_lyrics", playlist_name, "json"
    )

    return playlist_with_lyrics


if __name__ == "__main__":
    pass
