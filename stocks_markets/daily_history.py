
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

    symbol = str(symbol).strip()

    df = capital_market.price_volume_and_deliverable_position_data(
        symbol=symbol,
        period=period
    )
    df.columns=['Symbol', 'Series', 'Date', 'PrevClose', 'OpenPrice', 'HighPrice', 'LowPrice', 'LastPrice', 
                'ClosePrice', 'AveragePrice', 'TotalTradedQuantity', 'TurnoverInRs', 'No.ofTrades', 'DeliverableQty', 'DlyQttoTradedQty']

    df_select = df[
        [
            'Symbol',
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

    # df_select = df_select.rename(
    #     columns={'ï»¿"Symbol"': 'Symbol'}
    # )

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




nse_stocks = pd.read_csv("/Users/savindrasingh/Desktop/codes/genai/stocks_markets/nse_companies_marketcap.csv")
nse_2026 = nse_stocks['symbol'].dropna().unique()


print(nse_2026)

# results = []
# for symbol in nse_stocks['symbol'].dropna():
#     symbol = str(symbol).strip()
#     print(f"Fetching data for symbol: {symbol}")


# for symbol in nse_stocks['symbol'].dropna():
#     symbol = str(symbol).strip()
#     print(f"Fetching data for symbol: {symbol}")
#     results.append(daily_history('symbol', period="6M"))

# results_df = pd.concat(results, ignore_index=True)
# results_df.to_csv("daily_history.csv", index=False)
# print(results_df.head(20))


results_df = pd.DataFrame()

for symbol in nse_2026:
   
    print(f"Fetching data for symbol: {symbol}")
    print(f"Type of symbol: {type(symbol)}")
    df = capital_market.price_volume_and_deliverable_position_data(
    symbol=symbol,
    period="1Y")
    print(df.head(5))

    # df = daily_history(symbol=symbol, period="6M")

    df.columns=['Symbol', 'Series', 'Date', 'PrevClose', 'OpenPrice', 'HighPrice', 'LowPrice', 'LastPrice', 
                    'ClosePrice', 'AveragePrice', 'TotalTradedQuantity', 'TurnoverInRs', 'No.ofTrades', 'DeliverableQty', 'DlyQttoTradedQty']
    
    df_select = df[
        [
            'Symbol',
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

    print(df_select.head(5))


    df_select["Date"] = pd.to_datetime(df_select["Date"])

    numeric_columns = [
        'PrevClose',
        'OpenPrice',
        'HighPrice',
        'LowPrice',
        'LastPrice',
        'ClosePrice'
    ]

    print(df_select.head(6))
    
    # for column in numeric_columns:
    #     df_select[column] = (
    #         df_select[column]
    #         .str.replace(',', '', regex=False)
    #         .astype(float)
    #     )
    
    df_select.sort_values("Date", inplace=True)
    df_select.reset_index(drop=True, inplace=True)
    print(results_df.head(20))
    






    results_df = pd.concat([results_df, df_select], ignore_index=True)

print(results_df.head(20))
results_df.to_csv("dail_history_1Y.csv", index=False)





  









