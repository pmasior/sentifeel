from intermediate_constants import constants
from io_helper import cacher, cache_handler
from text_translator import text_translator
from type_defs.adapter.types import PlaylistWithLyrics, PlaylistsWithLyrics


def _get_playlist_translations(playlist: PlaylistWithLyrics) -> PlaylistWithLyrics:
    cache_handler.make_intermediate_directory(constants.I8_TRANSLATIONS_TXT)
    songs_to_analyze = []
    for song in playlist:
        lyrics = cache_handler.open_from_intermediate_directory(
            constants.I5_TEKSTOWO_TXT, song["song_id"], "txt"
        )
        songs_to_analyze.append({"id": song["song_id"], "text": lyrics})
    songs_with_translations = text_translator.translate_texts(songs_to_analyze, "en")
    for song, translation in zip(playlist, songs_with_translations):
        translation_text = translation["translations"][0]["text"]
        cache_handler.save_to_intermediate_directory(
            translation_text, constants.I8_TRANSLATIONS_TXT, song["song_id"], "txt"
        )
    return playlist


def _get_playlists_translations(playlists: PlaylistsWithLyrics) -> PlaylistsWithLyrics:
    playlists_with_translations = {}
    for playlist in playlists:
        playlists_with_translations[playlist] = _get_playlist_translations(
            playlists[playlist]
        )
    return playlists_with_translations


def get_playlist_translations(
    playlist: PlaylistWithLyrics, playlist_name: str
) -> PlaylistWithLyrics:
    return cacher.cache2(
        _get_playlist_translations,
        constants.I9_PLAYLIST_WITH_TRANSLATIONS,
        playlist_name,
        "json",
    )(playlist)


def get_playlists_translations(
    playlists: PlaylistsWithLyrics, playlists_name: str
) -> PlaylistsWithLyrics:
    return cacher.cache2(
        _get_playlists_translations,
        constants.IA_PLAYLISTS_WITH_TRANSLATIONS,
        playlists_name,
        "json",
        should_read_from_cache=False,
    )(playlists)


if __name__ == "__main__":
    pass
