from typing import Union, List, Dict
import time

import requests


def wrapped_http_caller(
        method: str,
        url: str,
        data: Union[List, Dict] = None,
        headers: Dict = None,
        backoffs: int = 5
):
    headers = headers or {}
    request = _backoff_http_caller(**locals())
    return request.json()


def _backoff_http_caller(
        method: str,
        url: str,
        data: Union[List, Dict] = None,
        headers: Dict = None,
        backoffs: int = 5
):
    failed_requests = []
    for i in range(backoffs):
        req = requests.request(method=method, url=url, data=data, headers=headers)
        if req.status_code < 300:
            return req
        failed_requests.append(req)
    raise ConnectionError(f'API Call method: {method}, url: {url} failed due to '
                          f'{[request.reason for request in failed_requests]}')
