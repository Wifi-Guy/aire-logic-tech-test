from src.apis.lyrics import get_lyric_count
from unittest.mock import MagicMock


def test_get_lyric_count_passes():
    mocked_http_caller = MagicMock(return_value={'lyrics': 'Some good lyrics'})
    assert get_lyric_count('Tame Impala', 'The Less I know the better', http_caller=mocked_http_caller) == 3
