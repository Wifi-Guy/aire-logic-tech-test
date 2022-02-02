from src.apis.music_brains import get_artist_mbid, get_recordings
from unittest.mock import MagicMock
import pytest
from src.utilities.exceptions import *


def test_get_artist_mbid_passes():
    mocked_http_caller = MagicMock(return_value={'artists': [{'id': 'bob'}]})
    assert get_artist_mbid('test', http_caller=mocked_http_caller) == 'bob'


def test_get_artist_mbid_passes_picks_first_artist():
    mocked_http_caller = MagicMock(return_value={'artists': [{'id': 'bob'}, {'id': 'bobbette'}]})
    assert get_artist_mbid('test', http_caller=mocked_http_caller) == 'bob'


def test_get_artist_mbid_fails_no_artists_found():
    mocked_http_caller = MagicMock(return_value={'artists': []})
    with pytest.raises(NotFoundError):
        get_artist_mbid('test', http_caller=mocked_http_caller)


def test_get_recordings():
    mocked_http_caller = MagicMock(return_value={'recordings': [{'title': 'bob tests'}, {'title': 'bobbette tests'}]})
    assert get_recordings('test', http_caller=mocked_http_caller) == ['bob tests', 'bobbette tests']
