from typing import Any
from pathlib import Path
import csv
import math

RatesHistory = list[dict[str, Any]]

def load_rates_from_history(rates_file_path: Path) -> RatesHistory:
    rate_history: RatesHistory = []

    # with statement here is used so we don't have to close
    
    with open(rates_file_path, encoding="UTF-8") as rates_file:
        rates_file_csv = csv.DictReader(rates_file)

        for rate_row in rates_file_csv:
            rate_entry = { "Date": rate_row["Date"], "EUR": 1.0 }

            for rate_col in rate_row:
                if rate_col != "Date" and len(rate_col) > 0:
                    if rate_row[rate_col] == "N/A":
                        rate_entry[rate_col] = math.nan
                    else:
                        rate_entry[rate_col] = float(rate_row[rate_col])
                

            rate_history.append(rate_entry)



    return rate_history



