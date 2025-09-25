"""
Utility functions for data generation and preprocessing.
"""

import pdb
import pandas as pd
from datetime import datetime

def dict_to_csv(data, csv_name="output.csv"):
    """
    This function converts the json file provided by the BLS API and converts
    it to a csv.
    """
    data = data["Results"]["series"] # this is a list
    out = []
    for series in data:
        id = series['seriesID']
        for item in series['data']:
            row = []
            dt = date_convert(item['year'] + " " + item['periodName'])
            row.append(id)
            row.append(dt)
            row.append(item['value'])
            out.append(row)
    df = pd.DataFrame(out, columns=['item', 'date', 'value'])
    df.to_csv(csv_name, index=False)
            
            


def date_convert(s):
    """
    converts a string in the format '2023 December' into a datetime object
    """
    dt = datetime.strptime(s, "%Y %B")
    return dt
    

    
