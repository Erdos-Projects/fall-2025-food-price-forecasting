from data import *
from datetime import datetime

def main():
    BLS_test()

def BLS_test():
    print("Testing the BLS api object")
    api = BLS()
    # columns for "food at home" from https://www.bls.gov/cpi/additional-resources/cpi-item-aggregation.htm
    columns = "SEFA01, SEFA02, SEFA03, SEFB01, SEFB02, SEFB03, SEFB04, SEFC01, SEFC02, SEFC03, SEFC04, SEFD01, SEFD02, SEFD03, SEFD04, SEFE01, SEFF01, SEFF02, SEFG01, SEFG02, SEFH01, SEFJ01, SEFJ02, SEFJ03, SEFJ04, SEFK01, SEFK02, SEFK03, SEFK04, SEFL01, SEFL02, SEFL03, SEFL04, SEFM01, SEFM02, SEFM03, SEFN01, SEFN02, SEFN03, SEFP01, SEFP02, SEFR01, SEFR02, SEFR03, SEFS01, SEFS02, SEFS03, SEFT01, SEFT02, SEFT03, SEFT04, SEFT05, SEFT06"
    aggregates = "SFA11, SA0"
    columns = columns + ", " + aggregates
    columns = columns.split(", ")
    start = datetime(1979, 1, 1)
    end = datetime(2025, 7, 1)
    date_range = [start, end]
    df = api.get_data(columns, date_range, seasonal_adjust=True, mode='income', registration_key=True)
    print(df)

    print("Now testing the saving feature")
    df = api.get_data(columns, date_range, seasonal_adjust=True, save_path="./data/raw/CPI.csv", registration_key=True)
    df = api.get_data(columns, date_range, seasonal_adjust=True, save_path="./data/raw/income.csv", mode='income', registration_key=True)


if __name__ == "__main__":
    main()
