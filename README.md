# Personal Finance Tracker

A simple command-line application to track income and expenses, with visualization capabilities.

---

## Features

- Add new transactions with date, amount, category (Income/Expense), and optional description
- View transactions within a specified date range
- Display summary statistics (total income, total expenses, net savings)
- Visualize income and expenses over time with matplotlib plots
- Data persistence using CSV files

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/personal-finance-tracker.git
   cd personal-finance-tracker
   ```
2. Install the required dependencies:
   ```bash
   pip install pandas matplotlib
   ```

---

## Usage

Run the application:
  ```bash
  python main.py
  ```

---

## Menu Options
#### Add a new transaction:
- Enter transaction details (date defaults to today)
- Amount must be positive
- Choose between Income (I) or Expense (E)
- Optional description field

#### View transactions and summary:
- Specify a date range (dd-mm-yyyy format)
- View all transactions in the period
- See summary statistics
- Option to visualize data with a plot

#### Exit the application

---

## Data Storage
All transactions are stored in finance_data.csv with the following columns:
- date (dd-mm-yyyy format)
- amount (float)
- category (Income/Expense)
- description (optional text)

---

## Code Structure
1. main.py: Contains the main application logic and menu system
- CSV class handles all file operations
- plot_transactions() generates visualizations

2. data_entry.py: Contains input validation functions
- Date validation (dd-mm-yyyy format)
- Positive amount validation
- Category validation (I/E)
- Description input

---

## Dependencies
1. Python 3.x
2. pandas
3. matplotlib

---

## Example Usage
```text
1. Add a new transaction
2. View transactions and a summary within a date range
3. Exit
Enter your choice (1-3): 1
Enter the date of the transaction (dd-mm-yyyy) or click 'Enter' for today's date: 
Enter the amount: 500
Enter the category ('I' for Income or 'E' for Expense) I
Enter a description (optional): Salary
Entry added successfully
```

---

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and share this project with proper attribution.
