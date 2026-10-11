from nselib import capital_market
from datetime import datetime, timedelta
import pandas as pd

def fetch_stock(symbol="TCS", period="5Y"):
    period_days = {
        "1M": 30,
        "3M": 90,
        "6M": 180,
        "1Y": 365,
        "2Y": 730,
        "5Y": 1825
    }

    end_date = datetime.today()
    start_date = end_date - timedelta(days=period_days[period])

    df = capital_market.price_volume_and_deliverable_position_data(
        symbol=symbol,
        from_date=start_date.strftime("%d-%m-%Y"),
        to_date=end_date.strftime("%d-%m-%Y")
    )

    return df

nse_stocks = pd.read_csv("/Users/savindrasingh/Desktop/codes/genai/stocks_markets/nse_companies_marketcap.csv")
nse_2026 = nse_stocks['symbol'].dropna().unique()
nse_data_5y = pd.concat(
    [fetch_stock(symbol, "5Y") for symbol in nse_2026],
    ignore_index=True
)

nse_data_5y.to_csv("nse_data_5y.csv", index=False)

print(nse_data_5y.head(20))


