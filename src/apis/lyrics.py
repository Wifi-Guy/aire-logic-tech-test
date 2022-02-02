from src.utilities.http_caller import wrapped_http_caller


def get_lyric_count(artist_name: str, song_name: str, http_caller: wrapped_http_caller = wrapped_http_caller):
    lyrics = http_caller(
        method='GET',
        url=f'https://api.lyrics.ovh/v1/{artist_name}/{song_name}'
    )['lyrics']
    return len(lyrics.split(' '))
