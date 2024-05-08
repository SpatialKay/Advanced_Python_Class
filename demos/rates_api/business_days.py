from datetime import date, timedelta
import holidays

def business_days(start: date, end: date) -> list[date]:
    us_holidays = holidays.CountryHoliday("US")
    date_diff = end - start
    business_days_list = []
    for day in range(date_diff.days + 1):
        the_date = start + timedelta(day)
        if the_date.weekday() < 5 and the_date not in us_holidays:
            business_days_list.append(the_date)
    return business_days_list

if __name__ == "__main__":
    print(business_days(date(2024, 5, 1), date(2024, 5, 6)))


