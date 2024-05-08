from contextlib import contextmanager
import multiprocessing as mp
from typing import Generator, Callable

import requests
from requests.exceptions import RequestException


@contextmanager
def api_server(
    health_check_url: str, api_start_func: Callable[[], None]
) -> Generator[None, None, None]:
    api_process = mp.Process(target=api_start_func)
    api_process.start()

    while True:
        try:
            requests.get(health_check_url, timeout=2)
            break
        except ConnectionError:
            continue
        except RequestException:
            continue
    yield

    api_process.terminate()
