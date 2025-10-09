import pdb, os
import pandas as pd
import requests
import json
from datetime import datetime
from .utils import dict_to_csv
import warnings

class BLS():
    def __init__(self):
        pass

    def get_data(self, id_list, date_range, seasonal_adjust=False, save_path=None, mode='cpi', registration_key=False):
        self.id_list = id_list
        self.date_range = date_range
        self.seasonal_adjust = seasonal_adjust
        self.mode = mode
        self.registration_key = registration_key

        date_list = self._get_date_list()
        columns = self._get_columns()
        df_list = []
        for dates in date_list:
            df_list.append(self.fetch(columns, dates))

        df = pd.concat(df_list).drop_duplicates()
        df = df.pivot(index='date', columns='item', values='value')
        mask = (df.index >= date_range[0]) & (df.index <= date_range[1])
        df = df[mask]
        if save_path is not None:
            df.to_csv(save_path, index=True)
        else:
            return df

    def fetch(self, columns, date_range):
        headers = {'Content-type': 'application/json'}
        if self.mode == 'income':
            columns = ['LEU0252881500']  # this is the series id for weekly income unadjusted
        json_payload = {"seriesid": columns,
                        "startyear": date_range[0],
                        "endyear": date_range[1]}
        if self.registration_key:
            key = os.getenv("BLS_KEY")
            json_payload['registrationkey'] = key

        data = json.dumps(json_payload)
        p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/',
                          data=data,
                          headers=headers)
        json_data = json.loads(p.text)
        df = self._convert_to_df(json_data)
        # test if json has warning messages
        if len(json_data['message']) > 0:
            warning_message = "BLS request returned a user warning: " + str(json_data['message'])
            warnings.warn(warning_message, category=UserWarning)
        return df

    def _convert_to_df(self, data):
        if data['status'] == 'REQUEST_NOT_PROCESSED':
            message = "Number of daily api calls has reached the limit: " + str(data['message'])
            raise RuntimeError(message)
        data = data["Results"]["series"]  # this is a list
        out = []
        for series in data:
            id = series['seriesID']
            for item in series['data']:
                row = []
                if self.mode == 'income':
                    s = item['year'] + " " + self._quarter_to_month(item['periodName'])
                else:
                    s = item['year'] + " " + item['periodName']
                    
                dt = datetime.strptime(s, "%Y %B")
                row.append(id)
                row.append(dt)
                row.append(item['value'])
                out.append(row)
        df = pd.DataFrame(out, columns=['item', 'date', 'value'])
        return df
        # df = df.pivot(index='date', columns='item', values='value')
        # df.to_csv(csv_name, index=True)

    def _get_date_list(self):
        date_range_list = []
        start_date = self.date_range[0]
        end_date = self.date_range[1]
        if (end_date.year - start_date.year) > 10:
            # make list of date ranges in chunks of 10 years
            out = []
            start_year = start_date.year
            end_year = end_date.year
            temp_year = start_year + 9
            while True:
                out.append([str(start_year), str(temp_year)])
                start_year = temp_year + 1
                temp_year = temp_year + 9
                if temp_year >= end_year:
                    out.append([str(start_year), str(end_year)])
                    break
            return out
        else:
            return [[str(start_date.year), str(end_date.year)]]

    def _quarter_to_month(self, s):
        quarter = int(s[0])
        if quarter == 1:
            return 'January'
        elif quarter == 2:
            return 'April'
        elif quarter == 3:
            return 'July'
        elif quarter == 4:
            return 'October'
        else:
            return None


    def _get_columns(self):
        if self.seasonal_adjust:
            prefix = "CUSR0000"
        else:
            prefix = "CUUR0000"
        out = []
        for name in self.id_list:
            out.append(prefix+name)
        return out

if __name__ == "__main__":
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
    #df = api.get_data(columns, date_range, seasonal_adjust=True)
    #print(df)

    print("Now testing the saving feature")
    df = api.get_data(columns, date_range, seasonal_adjust=True, save_path="./example_data.csv")
    

