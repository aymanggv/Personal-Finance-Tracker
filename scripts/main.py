import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_description
import matplotlib.pyplot as plt # Only need pyplot for this


class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    DATE_FORMAT = "%d-%m-%Y"
    
    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns = cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index = False)
            
    
    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        
        with open(cls.CSV_FILE, "a", newline="") as csvfile: # a moves cursor to end
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully")
        
        
    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df["date"] = pd.to_datetime(df["date"], format = cls.DATE_FORMAT)
        start_date = datetime.strptime(start_date, cls.DATE_FORMAT)
        end_date = datetime.strptime(end_date, cls.DATE_FORMAT)
        
        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df = df.loc[mask]
        
        if filtered_df.empty:
            print("No transactions found")
        else:
            print(f"Transactions from {start_date.strftime(cls.DATE_FORMAT)} to {end_date.strftime(cls.DATE_FORMAT)}")
            print(filtered_df.to_string(index= False, formatters = {"date": lambda x: x.strftime(cls.DATE_FORMAT)}))
            
        total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
        total_expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()
        print("\nSummary:")
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expense: ${total_expense:.2f}")
        print(f"Net Savings: ${(total_income - total_expense):.2f}")
        return filtered_df
        
        

def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of the transaction (dd-mm-yyyy) or click 'Enter' for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    
    CSV.add_entry(date, amount, category, description)



def plot_transactions(df):
    df.set_index("date", inplace = True)
    income_df = df[df["category"] == "Income"].resample("D").sum().reindex(df.index, fill_value=0) # Resample is kinda like refilling the days in between. So all the empty days will be marked as 0.
    expense_df = df[df["category"] == "Expense"].resample("D").sum().reindex(df.index, fill_value=0)
    plt.figure(figsize = (10,5))
    plt.plot(income_df.index, income_df["amount"], label = "Income", color = "g")
    plt.plot(expense_df.index, expense_df["amount"], label = "Expense", color = "r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expenses Over Time")
    plt.legend
    plt.grid(True)
    plt.show()
    

def main():
    while True:
        print("\n1. Add a new transaction")
        print("\n2. View transactions and a summary within a date range")
        print("\n3. Exit")
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            add()
        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yyyy)")
            end_date = get_date("Enter the end date (dd-mm-yyyy)")
            df = CSV.get_transactions(start_date, end_date)
            if input("Do you want to see a plot? (y/n)").lower() == "y":
                plot_transactions(df)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Inva;id choice. Enter 1, 2 or 3: ")
            

if __name__ == "__main__":
    main()