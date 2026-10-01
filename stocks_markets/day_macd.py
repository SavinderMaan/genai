import pandas as pd
from nselib import capital_market

def fetch_tcs(period="6M"):
    """
    Fetch historical NSE data for TCS using nselib.
    period options: 1M, 3M, 6M, 1Y, 2Y, 5Y
    """
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

    df["date"] = pd.to_datetime(df["date"])
    df['close'] = df['close'].str.replace(',', '').astype(float)
    df.sort_values("date", inplace=True)

    return df


def compute_macd(df):
    """
    Compute MACD (12, 26, 9) manually using pandas.
    """

    # EMA calculations
    df["EMA12"] = df["close"].ewm(span=12, adjust=False).mean()
    df["EMA26"] = df["close"].ewm(span=26, adjust=False).mean()

    # MACD Line
    df["MACD"] = df["EMA12"] - df["EMA26"]

    # Signal Line (9‑period EMA of MACD)
    df["Signal"] = df["MACD"].ewm(span=9, adjust=False).mean()

    # Histogram
    df["Hist"] = df["MACD"] - df["Signal"]

    return df


def detect_macd_cross(df):
    """
    Detect bullish/bearish MACD crossovers.
    """

    df["bullish_cross"] = (
        (df["MACD"] > df["Signal"]) &
        (df["MACD"].shift(1) < df["Signal"].shift(1))
    )

    df["bearish_cross"] = (
        (df["MACD"] < df["Signal"]) &
        (df["MACD"].shift(1) > df["Signal"].shift(1))
    )

    latest = df.iloc[-1]

    if latest["bullish_cross"]:
        return "Bullish MACD crossover"
    elif latest["bearish_cross"]:
        return "Bearish MACD crossover"
    else:
        return "No fresh crossover"


def run_macd_scan():
    df = fetch_tcs(period="6M")
    df = compute_macd(df)
    signal = detect_macd_cross(df)

    print("\n=== TCS (NSE) MACD Signal ===")
    print(signal)
    print("\nLatest MACD values:")
    print(df[["date", "MACD", "Signal", "Hist"]].tail())


# Run
run_macd_scan()
