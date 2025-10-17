import pandas as pd
import pdb, os
from datetime import datetime
from dateutil.relativedelta import relativedelta

def n_year_splitter(df, n=5, save_path=None):
    """
    returns splits for
    the last n year. That is, if 2025-07-01 is the max date and n = 2
    then the training splits will be
    train1 = dates <= 2023-07-01
    test1 = 2023-07-01 < dates <= 2024-07-01
    train2 = dates <= 2024-07-01
    test2 = 2024-07-01 < dates <= 2025-07-01

    if save_path is None, then function returns a generator object
    else it saves all data as csv files
    """
    df.index = pd.to_datetime(df.index)
    #final_date = datetime.strptime(df.index.max(), "%Y-%m-%d")
    final_date = df.index.max()
    dt = final_date - relativedelta(years=n+1)
    train = []
    test = []
    for i in range(n):
        dt = dt + relativedelta(years=1)
        test_mask = (df.index > dt) & (df.index <= (dt + relativedelta(years=1)))
        test_indices = df.index[test_mask]
        train_mask = df.index <= dt
        train_indices = df.index[train_mask]
        if save_path is None:
            train.append(train_indices)
            test.append(test_indices)
        else:
            train_name = os.path.join(save_path, f"split_{i}_train.csv")
            test_name = os.path.join(save_path, f"split_{i}_test.csv")
            df.loc[train_indices].to_csv(train_name)
            df.loc[test_indices].to_csv(test_name)
    if save_path is None:
        return train, test


if __name__ == "__main__":
    data_path = "../data/processed/"
    data_name = "CPI.csv"
    path = os.path.join(data_path, data_name)
    df = pd.read_csv(path, index_col='date')
    n_year_splitter(df, n=5, save_path=data_path)
    pdb.set_trace()
