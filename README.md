# Stock Buy/Sell Signal Generator

## Project Description

This project reads Daily_REL.xlsx and Weekly_REL.xlsx files and generates Buy and Sell signals automatically based on predefined conditions.

## Buy Condition

If Daily Close > Last Weekly High

Generate Buy Signal

## Sell Condition

If Daily Close < Last Weekly Low

Generate Sell Signal

## Output Files

- Buy.xlsx
- Sell.xlsx
- Day_1_REL.xlsx

## Technologies Used

- Python
- Pandas
- OpenPyXL

## How to Run

Open Terminal and run:

```bash
python trade.py
```