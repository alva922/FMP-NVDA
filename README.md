# FMP-NVDA
Fundamental Analysis of NVIDIA using FMP API in Python

fmp.get_quote('NVDA')
[{'symbol': 'NVDA',
  'name': 'NVIDIA Corporation',
  'price': 893.98,
  'changesPercentage': 1.0661,
  'change': 9.43,
  'dayLow': 850.12,
  'dayHigh': 905.37,
  'yearHigh': 974,
  'yearLow': 253.81,
  'marketCap': 2234950000000,
  'priceAvg50': 708.781,
  'priceAvg200': 514.4562,
  'exchange': 'NASDAQ',
  'volume': 66520583,
  'avgVolume': 51110326,
  'open': 866,
  'previousClose': 884.55,
  'eps': 11.94,
  'pe': 74.87,
  'earningsAnnouncement': '2024-05-22T10:59:00.000+0000',
  'sharesOutstanding': 2500000000,
  'timestamp': 1710878400}]

print(msft_info_df)
symbol                                                          NVDA
price                                                         893.98
beta                                                           1.725
volAvg                                                      51110326
mktCap                                                 2234950000000
lastDiv                                                         0.16
range                                                   253.81-974.0
changes                                                         9.43
companyName                                       NVIDIA Corporation
currency                                                         USD
cik                                                       0001045810
isin                                                    US67066G1040
cusip                                                      67066G104
exchange                                        NASDAQ Global Select
exchangeShortName                                             NASDAQ
industry                                              Semiconductors
website                                       https://www.nvidia.com
description        NVIDIA Corporation provides graphics, and comp...
ceo                                              Mr. Jen-Hsun  Huang
sector                                                    Technology
country                                                           US
fullTimeEmployees                                              29600
phone                                                   408 486 2000
address                                    2788 San Tomas Expressway
city                                                     Santa Clara
state                                                             CA
zip                                                            95051
dcfDiff                                                    339.96848
dcf                                                       554.011519
image              https://financialmodelingprep.com/image-stock/...
ipoDate                                                   1999-01-22
defaultImage                                                   False
isEtf                                                          False
isActivelyTrading                                               True
isAdr                                                          False
isFund                                                         False

print(msft_info_df)
symbol                                NVDA
date                            2024-03-19
rating                                  S-
ratingScore                              5
ratingRecommendation            Strong Buy
ratingDetailsDCFScore                    3
ratingDetailsDCFRecommendation     Neutral
ratingDetailsROEScore                    5
ratingDetailsROERecommendation  Strong Buy
ratingDetailsROAScore                    5
ratingDetailsROARecommendation  Strong Buy
ratingDetailsDEScore                     3
ratingDetailsDERecommendation      Neutral
ratingDetailsPEScore                     5
ratingDetailsPERecommendation   Strong Buy
ratingDetailsPBScore                     5
ratingDetailsPBRecommendation   Strong Buy

Credits:
https://benjaq.medium.com/a-simple-guide-how-to-use-the-financial-modeling-prep-api-in-python-b3e03e742fb8
https://medium.com/@slisowski/support-your-algorithmic-trading-with-fundamental-data-e81781b10d9d
https://pypi.org/project/fmp-python/
https://github.com/ddalgotrader/support_trading_fundamental_data/blob/main/FmpConnector.py

print(tesla_info_df)

  date symbol reportedCurrency         cik fillingDate  \
0  2024-01-28   NVDA              USD  0001045810  2024-02-21   
1  2023-01-29   NVDA              USD  0001045810  2023-02-24   
2  2022-01-30   NVDA              USD  0001045810  2022-03-18   
3  2021-01-31   NVDA              USD  0001045810  2021-02-26   
4  2020-01-26   NVDA              USD  0001045810  2020-02-20   

          acceptedDate calendarYear period  cashAndCashEquivalents  \
0  2024-02-21 16:36:57         2024     FY              7280000000   
1  2023-02-24 17:23:43         2023     FY              3389000000   
2  2022-03-17 20:33:34         2022     FY              1990000000   
3  2021-02-26 17:03:14         2021     FY               847000000   
4  2020-02-20 16:38:18         2020     FY             10896000000   

   shortTermInvestments  ...  totalStockholdersEquity  totalEquity  \
0           18704000000  ...              42978000000  42978000000   
1            9907000000  ...              22101000000  22101000000   
2           19218000000  ...              26612000000  26612000000   
3           10714000000  ...              16893000000  16893000000   
4               1000000  ...              12204000000  12204000000   

   totalLiabilitiesAndStockholdersEquity  minorityInterest  \
0                            65728000000                 0   
1                            41182000000                 0   
2                            44187000000                 0   
3                            28791000000                 0   
4                            17315000000                 0   

   totalLiabilitiesAndTotalEquity  totalInvestments    totalDebt     netDebt  \
0                     65728000000       20250000000  11056000000  3776000000   
1                     41182000000       10206000000  11855000000  8466000000   
2                     44187000000       19484000000  11687000000  9697000000   
3                     28791000000       10858000000   7597000000  6750000000   
4                     17315000000           1000000   2552000000 -8344000000   

                                                link  \
0  https://www.sec.gov/Archives/edgar/data/104581...   
1  https://www.sec.gov/Archives/edgar/data/104581...   
2  https://www.sec.gov/Archives/edgar/data/104581...   
3  https://www.sec.gov/Archives/edgar/data/104581...   
4  https://www.sec.gov/Archives/edgar/data/104581...   

                                           finalLink  
0  https://www.sec.gov/Archives/edgar/data/104581...  
1  https://www.sec.gov/Archives/edgar/data/104581...  
2  https://www.sec.gov/Archives/edgar/data/104581...  
3  https://www.sec.gov/Archives/edgar/data/104581...  
4  https://www.sec.gov/Archives/edgar/data/104581...  

[5 rows x 54 columns]
