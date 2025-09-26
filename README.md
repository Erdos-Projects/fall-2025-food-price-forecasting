# fall-2025-food-price-forecasting
Team project: fall-2025-food-price-forecasting
Team Member: [Duncan Bennett](https://github.com/tai-bennett), [Ray Hagimoto](), [Zhaodong Cai](), [Yoocheol Choi](), [Francis Baffour-Awuah Junior]()

# Table of Contents
1. [Introduction](#Introduction)
2. [Dataset Generation](#Dataset-Generation)
3. [Exploratory Data Analysis](#Exploratory-Data-Analysis)
4. [Modeling Approach](#Modeling-Approach)
5. [Results](#Results)
6. [Future Work](#Future-Work)
7. [Description of Repository](#Description-of-Repository)

## Introduction
The Consumper Price Index (CPI) is a monthly index that measures the average change in prices of a market basket
of goods and services bought by urban consumers. It is a weighted average that is currently
constructed from over 7700 basic indexes, which correspond to 32 geographic areas
segmented into 75 primary sampling units (PSUs). 

These indexes are used by the government to assess inflation, measure economic health and aid in decision making such as tax brackets, government subsidies, interest rates and more. Forecasting these values gives decision maker more time to make informed decision crucial for policy to respond timely.

Our goal is to forecast the basic indexes relevant to food.
## Dataset Generation
Data is gathered through the BLS website and their api. All data is public. Since most indexes are updated monthly, we will use an automated pipeline that periodically pulls and preprocessing data from the BLS.

CSV files are ignored by github in this repo. In order to download the data navigate to src/data and run the bls_api.py file.
## Exploratory-Data-Analysis
## Modeling-Approach
## Results
## Future Work
## Description of Repository
