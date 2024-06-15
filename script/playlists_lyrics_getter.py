import intermediate_files_handler
import playlist_lyrics_getter


def get_playlists_lyrics(playlists, playlists_name):
    intermediate_files_handler.make_intermediate_directory("7_playlists_with_lyrics")

    playlists_with_lyrics = {}
    for playlist in playlists:
        playlists_with_lyrics[playlist] = playlist_lyrics_getter.get_playlist_lyrics(
            playlists[playlist], playlist
        )
    intermediate_files_handler.save_to_intermediate_directory(
        playlists_with_lyrics, "7_playlists_with_lyrics", playlists_name, "json"
    )

    return playlists_with_lyrics


if __name__ == "__main__":
    pass
