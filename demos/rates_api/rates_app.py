import math
from flask import Flask, Response, abort, jsonify, request
from pathlib import Path

from rates_api.rates_data import load_rates_from_history


def start_rates_api() -> None:
    rates_file_path = Path("../data/rates.csv")
    rates = load_rates_from_history(rates_file_path)
    print(len(rates))

    app = Flask(__name__)

    @app.route("/check")
    def health_check() -> str:
        return "READY"

    # URL: http://127.0.0.1:5050/api/2021-04-08?base=INR&symbols=USD,EUR

    @app.route("/api/<rate_date>")
    def rates_by_date(rate_date: str) -> Response:
        for rate in rates:
            if rate["Date"] == rate_date:
                base_country = request.args.get("base", "EUR")

                if "symbols" in request.args:
                    country_symbols = request.args["symbols"].split(",")
                else:
                    # if the "symbols" is omitted from the request, then
                    # return all symbols
                    country_symbols = [col for col in rate if col != "Date"]

                country_rates = {
                    country_code: country_rate / rate[base_country]
                    for (country_code, country_rate) in rate.items()
                    if country_code != "Date"
                    and country_code in country_symbols
                    and not math.isnan(country_rate)
                }

                return jsonify(
                    {
                        "date": rate["Date"],
                        "base": base_country,
                        "rates": country_rates,
                    }
                )

        abort(404)

    app.run(port=8080)


if __name__ == "__main__":
    start_rates_api()
