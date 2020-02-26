import json
from importlib.resources import path
from typing import Dict

import pylyrics3


def save_manowar_lyrics():
    manowar_lyrics = pylyrics3.get_artist_lyrics('manowar')

    # filter non-english
    filtered = {song: lyrics for song, lyrics in manowar_lyrics.items() if 'Version' not in song}
    with path('data', 'manowar.json') as file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(filtered, file)


def get_manowar_lyrics() -> Dict[str, str]:
    with path('data', 'manowar.json') as file_path:
        with open(file_path, 'rt', encoding='utf-8') as file:
            manowar_lyrics = json.load(file)
            filtered = {song: lyrics for song, lyrics in manowar_lyrics.items() if 'Version' not in song}
    return filtered


if __name__ == "__main__":
    lyrics = get_manowar_lyrics()
    print(lyrics)
