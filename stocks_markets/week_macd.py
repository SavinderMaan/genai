import pandas as pd
from nselib import capital_market

def fetch_tcs_weekly(period="1Y"):
    """
    Fetch weekly NSE data for TCS.

    period options: 1M, 3M, 6M, 1Y, 2Y, 5Y
    """

    # Fetch daily data
    df = capital_market.price_volume_and_deliverable_position_data(
        symbol="TCS",
        period=period
    )

    # Standardize column names
    df.rename(columns={
        "Date": "date",
        "Open Price": "open",
        "High Price": "high",
        "Low Price": "low",
        "PrevClose": "close",
        "Total Traded Quantity": "volume"
    }, inplace=True)

    # Data cleaning
    df["date"] = pd.to_datetime(df["date"])

    for col in ["open", "high", "low", "close", "volume"]:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace(",", "", regex=False)
            .astype(float)
        )

    df.sort_values("date", inplace=True)

    # Set date as index
    df.set_index("date", inplace=True)

    # Convert daily candles to weekly candles
    weekly_df = df.resample("W-FRI").agg({
        "open": "first",
        "high": "max",
        "low": "min",
        "close": "last",
        "volume": "sum"
    })

    # Remove incomplete rows
    weekly_df.dropna(inplace=True)

    weekly_df.reset_index(inplace=True)

    return weekly_df

df_month=fetch_tcs_weekly(period="1Y")
print(df_month.head(20))


df = capital_market.price_volume_and_deliverable_position_data(
    symbol="TCS",
    period=period
)