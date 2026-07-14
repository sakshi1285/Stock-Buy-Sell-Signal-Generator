"""
-----------------------------------------
Stock Buy/Sell Signal Generator
-----------------------------------------
Author : Sakshi
Language : Python

Description:
Reads Daily and Weekly Excel files,
compares Daily Close with Weekly High/Low,
and generates Buy/Sell signals.
-----------------------------------------
"""

# ==========================
# Import Libraries
# ==========================

import pandas as pd
import os
from shutil import copyfile

# ==========================
# File Names
# ==========================

DAILY_FILE = "Daily_REL.xlsx"
WEEKLY_FILE = "Weekly_REL.xlsx"

BUY_FILE = "Buy.xlsx"
SELL_FILE = "Sell.xlsx"

DAY1_FILE = "Day_1_REL.xlsx"

# ==========================
# Read Excel Files
# ==========================

def read_excel():

    daily_df = pd.read_excel(DAILY_FILE, engine="openpyxl")
    weekly_df = pd.read_excel(WEEKLY_FILE, engine="openpyxl")

    # Remove extra spaces from column names
    daily_df.columns = daily_df.columns.str.strip()
    weekly_df.columns = weekly_df.columns.str.strip()

    return daily_df, weekly_df

# ==========================
# Generate Buy/Sell Signals
# ==========================

def generate_signals(daily_df, weekly_df):
    """
    Compare Daily Close with the last Weekly High and Low.
    """

    buy_records = []
    sell_records = []

    # Get the last record from Weekly sheet
    last_week = weekly_df.iloc[-1]

    weekly_high = last_week["High"]
    weekly_low = last_week["Low"]

    print("\nLast Weekly High :", weekly_high)
    print("Last Weekly Low  :", weekly_low)

    # Check every stock in Daily sheet
    for index, row in daily_df.iterrows():

        close_price = row["Close"]

        print("\nChecking :", row["Script_Name"])
        print("Close Price :", close_price)

        # BUY Condition
        if close_price > weekly_high:

            print("BUY Signal Generated")

            buy_records.append(row)

        # SELL Condition
        elif close_price < weekly_low:

            print("SELL Signal Generated")

            sell_records.append(row)

        else:

            print("No Signal")

    return buy_records, sell_records

# ==========================
# Save Buy and Sell Records
# ==========================

def save_buy_sell(buy_records, sell_records):
    """
    Save Buy and Sell records into separate Excel files.
    """

    # ---------- BUY ----------
    if len(buy_records) > 0:

        buy_df = pd.DataFrame(buy_records)

        buy_df.to_excel(
            BUY_FILE,
            index=False,
            engine="openpyxl"
        )

        print(f"\n✅ {BUY_FILE} created successfully.")

    else:

        print("\nNo Buy Signal found.")

    # ---------- SELL ----------
    if len(sell_records) > 0:

        sell_df = pd.DataFrame(sell_records)

        sell_df.to_excel(
            SELL_FILE,
            index=False,
            engine="openpyxl"
        )

        print(f"✅ {SELL_FILE} created successfully.")

    else:

        print("No Sell Signal found.")

# ==========================
# Update Day_1_REL.xlsx
# ==========================

def update_day1():
    """
    Create or update Day_1_REL.xlsx
    by copying Daily_REL.xlsx.
    """

    copyfile(DAILY_FILE, DAY1_FILE)

    print(f"✅ {DAY1_FILE} updated successfully.")

# ==========================
# Main Function
# ==========================

def main():

    # Read Excel files
    daily_df, weekly_df = read_excel()

    # Generate signals
    buy_records, sell_records = generate_signals(
        daily_df,
        weekly_df
    )

    # Save Buy and Sell Excel files
    save_buy_sell(
        buy_records,
        sell_records
    )

    # Update Day_1_REL.xlsx
    update_day1()

    print("\nProject Completed Successfully.")

# ==========================
# Program Starts Here
# ==========================

if __name__ == "__main__":
    main()