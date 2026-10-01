import pandas as pd
from nselib import capital_market


df = capital_market.price_volume_and_deliverable_position_data(
    symbol="TCS",
    period='6M'
)

df_select = df[['ï»¿"Symbol"', 'Series', 'Date', 'PrevClose', 'OpenPrice', 'HighPrice', 'LowPrice', 'LastPrice', 'ClosePrice']]
df_select = df_select.rename(columns={'ï»¿"Symbol"': 'Symbol'})
df_select["Date"] = pd.to_datetime(df_select["Date"])
for column in ['PrevClose', 'OpenPrice', 'HighPrice', 'LowPrice', 'LastPrice', 'ClosePrice']:
    df_select[column] = df_select[column].str.replace(',', '').astype(float)

df_select.sort_values("Date", inplace=True)

import pandas as pd
from nselib import capital_market


def daily_history(symbol, period="6M"):
    """
    Fetch historical daily NSE data for a given symbol.

    Parameters
    ----------
    symbol : str
        NSE stock symbol (e.g., 'TCS', 'INFY', 'RELIANCE')
    period : str
        Data period (e.g., '1M', '3M', '6M', '1Y', '2Y', '5Y')

    Returns
    -------
    tuple
        (df, df_select)
        df        : Original dataframe returned by nselib
        df_select : Cleaned dataframe with selected columns
    """

    df = capital_market.price_volume_and_deliverable_position_data(
        symbol=symbol,
        period=period
    )

    df_select = df[
        [
            'ï»¿"Symbol"',
            'Series',
            'Date',
            'PrevClose',
            'OpenPrice',
            'HighPrice',
            'LowPrice',
            'LastPrice',
            'ClosePrice'
        ]
    ].copy()

    df_select = df_select.rename(
        columns={'ï»¿"Symbol"': 'Symbol'}
    )

    df_select["Date"] = pd.to_datetime(df_select["Date"])

    numeric_columns = [
        'PrevClose',
        'OpenPrice',
        'HighPrice',
        'LowPrice',
        'LastPrice',
        'ClosePrice'
    ]

    for column in numeric_columns:
        df_select[column] = (
            df_select[column]
            .str.replace(',', '', regex=False)
            .astype(float)
        )

    df_select.sort_values("Date", inplace=True)
    df_select.reset_index(drop=True, inplace=True)

    return df_select


df=daily_history("TCS", period="6M")
print(df.head(20))

