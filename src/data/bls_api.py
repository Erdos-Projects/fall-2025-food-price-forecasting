"""
AUTHOR: Duncan Bennett
DESCRIPTION: This file consists of necessary functions to pull data from the BLS
website using their API. The code is based on the sample code provided at

https://www.bls.gov/developers/api_python.htm#python1

This file is still a work in progress.
TODO:
    - [ ] convert requested json file to csv format
    - [ ] create notebook friendly version/put into package to import
"""
import pdb
import requests
import json
import prettytable
def get_data(startyear, endyear, filename="data"):
    seriesid = get_series('CUUR0000')
    headers = {'Content-type': 'application/json'}
    data = json.dumps({"seriesid": seriesid,
                       "startyear": startyear,
                       "endyear": endyear})
    p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
    json_data = json.loads(p.text)
    output = open(filename + ".json", 'w')
    output.write(p.text)
    output.close()
#    for series in json_data['Results']['series']:
#        x = prettytable.PrettyTable(["series id", "year", "period", "value", "footnotes"])
#        seriesId = series['seriesID']
#        for item in series['data']:
#            year = item['year']
#            period = item['period']
#            value = item['value']
#            footnotes= ""
#            for footnote in item['footnotes']:
#                if footnote:
#                    footnotes = footnotes + footnote['text'] + ','
#            if 'M01' <= period <= 'M12':
#                x.add_row([seriesId, year, period, value, footnotes[0:-1]])
#        output = open(seriesId + '.txt', 'w')
#        output.write(x.get_string())
#        output.close()

def get_series(prefix):
    with open('item.txt', 'r') as file:
        items = file.read().splitlines()
    out = []
    for item in items:
        out.append(prefix + item)
    return out


if __name__ == "__main__":
    # series id for fresh fruits and veggies
    #seriesid = ["SEFK01", "SEFK02", "SEFK03", "SEFK04", "SEFL01", "SEFL02", "SEFL03", "SEFL04"]
    # series id
    #seriesid = ['CUUR0000SA0','SUUR0000SA0']
    seriesid = ['CUUR0000SEFK', 'CUUR0110SEFH',  'CUUR0000SA0']
    get_data("2011", "2013")


