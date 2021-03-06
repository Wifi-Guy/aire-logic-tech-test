import logging
from src.utilities.http_caller import wrapped_http_caller
from src.utilities.exceptions import NotSpecificEnoughError, NotFoundError
logger = logging.getLogger(__name__)


def get_artist_mbid(artist_name: str, http_caller: wrapped_http_caller = wrapped_http_caller):
    artist_list = http_caller(
        url=f'http://musicbrainz.org/ws/2/artist/?query=name:{artist_name}&fmt=json',
        method='GET'
    )['artists']
    if len(artist_list) == 0:
        raise NotFoundError('Artist Not Found')
    return artist_list[0]['id']


def get_recordings(artist_mbid: str, http_caller: wrapped_http_caller = wrapped_http_caller):
    recordings = http_caller(
        url=f'https://musicbrainz.org/ws/2/artist/{artist_mbid}?inc=recordings&fmt=json',
        method='GET'
    )['recordings']
    return [track['title'] for track in recordings]
