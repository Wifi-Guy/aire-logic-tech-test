import sys
sys.path.append('..')  # This is needed as Tox/Intellij Work Really well with src. but CLI apps dont

import argparse
import logging
from src.apis.music_brains import get_artist_mbid, get_recordings
from src.apis.lyrics import get_lyric_count
import statistics

logging.basicConfig(level=logging.INFO)


def calculate_average_lyrics_per_artist(artist_name):
    artist_mbid = get_artist_mbid(artist_name)
    artist_recordings = get_recordings(artist_mbid)
    lyric_count_list = []
    for song in artist_recordings:
        try:
            lyric_count_list.append(get_lyric_count(artist_name, song))
        except ConnectionError:
            print(f'Song {song} not found')
    return statistics.mean(lyric_count_list)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("artist_name")
    args = parser.parse_args()
    print(calculate_average_lyrics_per_artist(args.artist_name))
