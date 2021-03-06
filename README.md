# experiment-bull-market-best-day-of-month

Twitter: @calkinsdev

## Objective

I want to find out if there is an optimal day of the month to buy stock every month if I continued doing so for 10 - 30 years.  That's a long time I'd hate to miss out on money simply due to buying on the 27th vs the 12th.

## Background Information

1. As it stands there is a cyclical nature in SPY due to the OPEX events every month between 15th and 20th, quad witching, and Federal Reserve meetings announcing interest rates.
1. For the last 10 years the US has been in a bull market, but I chose that time frame because it's the extent of my professional working experience.
1. There are numerous studies and anecdotes that confirm buying and holding long term makes you profitable even if you do it poorly.
1. This does not include any serious recessions like "dot com" or "housing crisis" save for COVID in Mar 2020.
1. We are not accounting for dividends, this is price action only.
1. AMC only has 7 years of data.
1. We are only testing a subset of popular tickers found in SPY (except AMC and X as outliers).
1. We are not trying to time the market we are trying to optimize the day that we buy in every month for 10 years based on current market conditions.
1. The priced used is the closing price of 9/20 to sell off shares.

## Hypothesis

I think if I only purchased on a day that avoided known events that cause high volatility we can actually create better profits as long as we're consistent.  Especially since we're holding for so long.

## Materials/Procedures 

1. 10 year data provided by NASDAQ: https://www.nasdaq.com/market-activity/stocks/mnst/historical 
1. You can find the script used to process the data in `src/spy.py`.
1. I'd then run the command `python src/spy.py`, basically it buys one share, once per month, for 10 years.
1. Then I copy the data from `src/output.csv` into a Google spreadsheet that graphed the data from the 1st of the month all the way to the 31st.
1. https://docs.google.com/spreadsheets/d/1OVpWaR37AJl7D57HaHu2ch_XD7TmeASPwoA-h5nvnKc/edit?usp=sharing

## Observances

1. Even a once volatile stock like AMC has a predictable curve.
1. Tickers like WFC and T focused on putting out dividends did not fare well in this experiment having a scattered pattern.
1. You're pretty much always profitable if your profits come from the price on growth stocks and not dividends.
1. The middle of the month clearly has drops in it.
1. Dividend focused tickers have pretty either barely positive or negative outcomes.
1. Even leveraged tickers like TQQQ show similar behavior to growth tickers.

## Conclusions

1. The 13th almost always comes out as the most profitable day to buy stock from our sample.
1. You should check the ticker your buying for a historical growth trend.  WFC, T, and X did not fare well in this experiment.
