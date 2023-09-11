# Historic currency data

## IDS 706 mini-project 2

Created a python script that:
* uses yahoo finance to download historic data on currencies
* creates open, high, low, close dictionaries and dataframes
* computes each currency's high, low, mean, std dev and close for the given period

Running the script with dates Aug 14 2023 and Sep 08 2023 on USDMXN, EURUSD and NZDUSD returns the following:

usdmxn's current value is 17.58.
Between 14/Aug/23 and 08/Sep/23:
- usdmxn rose 3.43%
- usdmxn reached a low of 16.68 on 28 Aug 23
- usdmxn reached a high of 17.7 on 07 Sep 23
- usdmxn had an average and standard deviation of 17.04 and 0.24 over the period.
eurusd's current value is 1.07.
Between 14/Aug/23 and 08/Sep/23:
- eurusd dropped -2.25%
- eurusd reached a low of 1.07 on 07 Sep 23
- eurusd reached a high of 1.1 on 14 Aug 23
- eurusd had an average and standard deviation of 1.08 and 0.01 over the period.
nzdusd's current value is 0.59.
...
- nzdusd dropped -1.71%
- nzdusd reached a low of 0.59 on 05 Sep 23
- nzdusd reached a high of 0.6 on 01 Sep 23
- nzdusd had an average and standard deviation of 0.59 and 0.0 over the period.


