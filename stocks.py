import pandas as pd
from nselib import capital_market

# Fetch all NSE listed companies
df = capital_market.equity_list()

# List all columns in df
print(df.columns.tolist())

print(df)


# Select useful columns
df = df[[
    "SYMBOL",
    "NAME OF COMPANY"

]]

# Clean column names
df.columns = ["symbol", "company"]

# Show first 20 rows
print(df.head(20))

# Save to CSV (optional)
df.to_csv("nse_companies_marketcap.csv", index=False)
