# Stock Buy/Sell Signal Generator

## Project Description

This project reads two Excel files:

- Daily_REL.xlsx
- Weekly_REL.xlsx

The program compares the Daily Close price with the last Weekly High and Weekly Low.

### Buy Condition

If Daily Close > Last Weekly High

→ Record is saved in Buy.xlsx

### Sell Condition

If Daily Close < Last Weekly Low

→ Record is saved in Sell.xlsx

### Additional Output

A copy of the latest Daily_REL.xlsx is stored as Day_1_REL.xlsx for testing and comparison purposes.

## Technologies Used

- Python
- Pandas
- OpenPyXL

## How to Run

1. Install the required libraries:

```bash
pip install -r requirements.txt
```

2. Run the program:

```bash
python trade.py
```