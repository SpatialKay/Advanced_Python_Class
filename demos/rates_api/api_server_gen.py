from contextlib import contextmanager
import multiprocessing as mp
from typing import Generator, Callable
import time

import requests
from requests.exceptions import RequestException


@contextmanager
def api_server(
    health_check_url: str, api_start_func: Callable[[], None]
) -> Generator[None, None, None]:
    # 1

    def __abort(error_message: str = "unknown error occurred") -> None:
        print(f"API Server Error: {error_message}")
        # guard to ensure api_process is a process and not none
        if api_process:
            api_process.terminate()
        exit(-1)

    try:
        start_up_timeout_in_seconds = 1
        api_process = mp.Process(target=api_start_func)
        api_process.start()

        start_health_check = time.time()

        while True:
            try:
                requests.get(health_check_url, timeout=2)
                break
            except ConnectionError:
                if (
                    time.time() - start_health_check
                    > start_up_timeout_in_seconds
                ):
                    __abort(
                        f"failed to start within "
                        f"{start_up_timeout_in_seconds} second"
                    )
                continue
            except RequestException:
                if (
                    time.time() - start_health_check
                    > start_up_timeout_in_seconds
                ):
                    __abort(
                        f"failed to start within "
                        f"{start_up_timeout_in_seconds} second"
                    )
                continue
        # 2
        yield

    # 5
    except Exception as exc:
        print(f"API Server Error: {exc}")
    finally:
        api_process.terminate()
