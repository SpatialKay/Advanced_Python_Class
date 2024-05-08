import requests

from rates_api.api_server import api_server

# from rates_api.api_server_gen import api_server
from rates_api.rates_app import start_rates_api


def main() -> None:
    health_check_url = "http://127.0.0.1:8080/check"

    with api_server(health_check_url, start_rates_api):
        # 3
        # the api server function yields to this point
        resp = requests.get(
            "http://127.0.0.1:8080/api/2021-04-08?base=INR&symbols=USD,EUR"
        )
        print(resp.json())
        # 4
        # we call back into the api server function


if __name__ == "__main__":
    main()
