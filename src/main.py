import argparse
import logging

logging.basicConfig(level=logging.INFO)


def calculate_average_lyrics_per_artist(artist_name):
    raise NotImplementedError


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("artist_name")
    args = parser.parse_args()
    print(calculate_average_lyrics_per_artist(args.artist_name))
