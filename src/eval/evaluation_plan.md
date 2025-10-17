# Evaluation Plan
## Unit of Analysis
Each row of the data is a vector of CPI values for a certain year-month. 
## Split Strategy
We plan to evaluate model performance on forecasting the last $n=5$ years one year at a time. That is, if data is provided up through 2025-07 then splits take the form
- split_0_train : date <= 2020-07
- split_0_test : 2020-07 < date <= 2021-07
- split_1_train : date <= 2021-07
- split_1_test : 2021-07 < date <= 2022-07
- ...
- split_4_train : date <= 2024-07
- split_4_test : 2024-07 < date <= 2025-07
*Maybe add visual to illustrate splits*

The motiviation for these evaluation splits comes from the contextual motivation for forecasting. As a policy maker, you are forecasting and making predictions for the duration of your term to inform the policies you will propose and implement. Thus, forecasting in the 1-4 year range is desired with 1 year being more reliable than longer forecasts. 
