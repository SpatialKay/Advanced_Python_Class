import multiprocessing as mp
import time
from requests.exceptions import ConnectionError, RequestException
import requests
from typing import Callable, Any


# use snake case for the class name to be consistent with the generator
# version of this code
class api_server:
    def __init__(
        self, health_check_url: str, api_start_func: Callable[[], None]
    ):
        # 1
        self.health_check_url = health_check_url
        self.api_start_func = api_start_func
        self.api_process: mp.Process | None = None
        self.start_up_timeout_in_seconds = 1

    def __abort(self, error_message: str = "unknown error occurred") -> None:
        print(f"API Server Error: {error_message}")
        # guard to ensure api_process is a process and not none
        if self.api_process:
            self.api_process.terminate()
        exit(-1)

    def __enter__(self) -> None:
        # 2
        self.api_process = mp.Process(target=self.api_start_func)
        self.api_process.start()

        start_health_check = time.time()

        while True:
            try:
                requests.get(self.health_check_url, timeout=2)
                break
            except ConnectionError:
                if (
                    time.time() - start_health_check
                    > self.start_up_timeout_in_seconds
                ):
                    self.__abort(
                        f"failed to start within "
                        f"{self.start_up_timeout_in_seconds} second"
                    )
                continue
            except RequestException:
                if (
                    time.time() - start_health_check
                    > self.start_up_timeout_in_seconds
                ):
                    self.__abort(
                        f"failed to start within "
                        f"{self.start_up_timeout_in_seconds} second"
                    )
                continue
            except Exception as exc:
                self.__abort(str(exc))

        return

    def __exit__(self, exc_type: Exception, exc_val: Any, exc_tb: Any) -> None:
        # 5
        if exc_type is Exception:
            print(f"API Server Error: {exc_type}")
        if self.api_process is not None:
            self.api_process.terminate()
