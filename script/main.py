from adapter import (
    eurovision_rankings_getter,
    playlist_lyrics_getter,
    playlist_lyrics_analyzer,
)


if __name__ == "__main__":
    eurovision_rankings = eurovision_rankings_getter.get_eurovision_rankings()
    playlists_with_lyrics = playlist_lyrics_getter.get_playlists_lyrics(
        eurovision_rankings, "eurovision"
    )
    playlist_lyrics_analyzer.get_playlists_analysis(playlists_with_lyrics, "eurovision")
