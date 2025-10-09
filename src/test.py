from data import *
from datetime import datetime

def main():
    BLS_test()

def BLS_test():
    print("Testing the BLS api object")
    api = BLS()
    columns = ["SEFA01",
               "SEFA02",
               "SEFB01",
               "SEFB02",
               "SEFC01"]
    start = datetime(2001, 1, 1)
    end = datetime(2015, 4, 1)
    date_range = [start, end]
    df = api.get_data(columns, date_range, seasonal_adjust=True, mode='income', registration_key=True)
    print(df)

    print("Now testing the saving feature")
    df = api.get_data(columns, date_range, seasonal_adjust=True, save_path="./data/raw/CPI.csv", registration_key=True)
    df = api.get_data(columns, date_range, seasonal_adjust=True, save_path="./data/raw/income.csv", mode='income', registration_key=True)


if __name__ == "__main__":
    main()
