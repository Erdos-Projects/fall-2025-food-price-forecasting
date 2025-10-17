import pandas as pd
import pdb
from datetime import datetime
from dateutil.relativedelta import relativedelta

def n_year_splitter(df, n=5, save_path=None):
    """
    returns a generator object that produces training splits for
    the last n year. That is, if 2025-07-01 is the max date and n = 2
    then the training splits will be
    train1 = dates <= 2023-07-01
    test1 = 2023-07-01 < dates <= 2024-07-01
    train2 = dates <= 2024-07-01
    test2 = 2024-07-01 < dates <= 2025-07-01
    """
    df.index = pd.to_datetime(df.index)
    #final_date = datetime.strptime(df.index.max(), "%Y-%m-%d")
    final_date = df.index.max()
    dt = final_date - relativedelta(years=n+1)
    for i in range(n):
        dt = dt + relativedelta(years=1)
        test_mask = (df.index > dt) & (df.index <= (dt + relativedelta(years=1)))
        test_indices = df.index[test_mask]
        train_mask = df.index <= dt
        train_indices = df.index[train_mask]
        yield train_indices, test_indices
        


if __name__ == "__main__":
    data_path = "../data/processed/CPI.csv"
    df = pd.read_csv(data_path, index_col='date')
    g = n_year_splitter(df, n=5)
    pdb.set_trace()
