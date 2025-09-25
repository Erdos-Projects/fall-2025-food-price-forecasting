# Data
This folder contains all files used to download, preprocess and store data.
## Files
### bls-api.py
This file is the access point to the bls api as well as some preprocessing that is to be done in order to get nice csv files for the data. By default, the BLS website recommends access the data via requests which come in json format. We then convert the json into a csv.
### CU Files
The cu-item.tsv and cu-area.tsv come from the BLS website at TBA. The describe all item and area codes for the basic indexes. 
### item.txt
A text file containing item codes for the bls-api to pull. These codes are separated by \\n.
