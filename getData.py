import pandas as pd
import quiverquant
import yfinance as yf

# Initialize the quiverquant API with the token
quiver = quiverquant.quiver("04d16de546b15f153782fea2bd372137bf6d7774")

# Fetch the congressional trading data
df = quiver.congress_trading()

# Ensure TransactionDate is a datetime object
df["TransactionDate"] = pd.to_datetime(df["TransactionDate"])

# Filter the DataFrame for a specific date range
df = df[(df["TransactionDate"] >= "2024-01-01")]


# Function to parse the transaction range into lower and upper bounds
def parse_range(range_str):
    try:
        # Remove commas and dollar signs, then split the string
        start, end = range_str.replace(",", "").replace("$", "").split(" - ")
        return int(start), int(end)
    except ValueError:
        # Return None for invalid formats
        return None, None


# Initialize an empty list to store the return after trade
alist = []

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    try:
        startdate = row["TransactionDate"]

        # Attempt to download start price data
        try:
            startprice_df = yf.download(
                row["Ticker"], start=startdate, end=startdate + pd.Timedelta(days=1)
            )
        except Exception as e:
            print(f"Failed to download start price for {row['Ticker']}: {e}")
            startprice_df = pd.DataFrame()  # Create an empty DataFrame for handling

        # Attempt to download end price data
        try:
            endprice_df = yf.download(
                row["Ticker"], start="2024-01-01", end="2024-02-04"
            )
        except Exception as e:
            print(f"Failed to download end price for {row['Ticker']}: {e}")
            endprice_df = pd.DataFrame()  # Create an empty DataFrame for handling

        # Check if both DataFrames have data, then calculate the percentage change
        if not startprice_df.empty and not endprice_df.empty:
            startprice = float(startprice_df["Close"].iloc[-1])
            endprice = float(endprice_df["Close"].iloc[-1])
            pct_change = ((endprice - startprice) / startprice) * 100
            alist.append(
                round(pct_change, 2)
            )  # Round the percentage change to two decimal places
        else:
            alist.append(None)  # Use None for cases with no data
    except Exception as e:
        print(
            f"An error occurred for ticker {row['Ticker']} on {startdate.date()}: {e}"
        )
        alist.append(None)  # Use None for cases where an error occurred


# Add the calculated returns or error messages to the DataFrame
df["return_after_trade"] = alist


# Calculate estimated profit/loss range
def estimate_profit_loss(range_str, return_percent):
    lower, upper = parse_range(range_str)
    if lower is None or upper is None or return_percent in ["No data", "Error"]:
        return "No estimate"
    min_profit_loss = round(lower * (return_percent / 100), 2)
    max_profit_loss = round(upper * (return_percent / 100), 2)
    return f"${min_profit_loss} - ${max_profit_loss}"


# Convert the 'return_after_trade' column to numeric, setting errors='coerce' to turn non-numeric values into NaN
df["return_after_trade"] = pd.to_numeric(df["return_after_trade"], errors="coerce")


df["Estimate Profit/Loss"] = df.apply(
    lambda x: estimate_profit_loss(x["Range"], x["return_after_trade"]), axis=1
)

# Filter to show only rows with available data and positive return after trade
filtered_df = df[
    df["return_after_trade"].apply(lambda x: isinstance(x, (int, float)) and x > 0)
]

# Print the DataFrame
print(
    filtered_df[
        [
            "Representative",
            "TransactionDate",
            "Ticker",
            "Transaction",
            "Range",
            "return_after_trade",
            "Estimate Profit/Loss",
        ]
    ]
)

