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

df = fetch_stock("TCS", "5Y")

df.to_csv("TCS_5Y.csv", index=False)

print(df.shape)
