# experiment-bull-market-best-day-of-month

Twitter: @calkinsdev

## Objective

I want to find out if there is an optimal day of the month to buy stock every month if I continued doing so for 10 - 30 years.  That's a long time I'd hate to miss out on money simply due to buying on the 27th vs the 12th.

## Background Information

As it stands there is a cyclical nature in SPY due to the OPEX events every month between 15th and 20th, quad witching, and Federal Reserve meetings announcing interest rates.

For the last 10 years the US has been in a bull market, but I chose that time frame because it's the extent of my professional working experience.

There are numerous studies and anecdotes that confirm buying and holding long term makes you profitable even if you do it poorly.

This does not include any serious recessions like "dot com" or "housing crisis" save for COVID in Mar 2020.

## Hypothesis

I think if I only purchased on a day that avoided known events that cause high volatility we can actually create better profits as long as we're consistent.  Especially since we're holding for so long.

## Materials/Procedures 

10 year data provided by NASDAQ: https://www.nasdaq.com/market-activity/stocks/mnst/historical 

You can find the script used to process the data in `src/spy.py`.

I'd then run the command `python spy.py`.