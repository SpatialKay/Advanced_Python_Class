from datetime import date
import requests
from rates_api.business_days import business_days


def main() -> None:
    start_date = date(2021, 3, 1)
    end_date = date(2021, 3, 15)

    rates_api_responses: list[str] = []
    for business_day in business_days(start_date, end_date):
        resp = requests.get(
            (
                f"http://127.0.0.1:8080/api/{business_day}"
                "?base=USD&symbols=EUR"
            )
        )

        if resp.status_code != 200:
            continue

        rates_api_responses.append(resp.json())

    print(rates_api_responses)


if __name__ == "__main__":
    main()
