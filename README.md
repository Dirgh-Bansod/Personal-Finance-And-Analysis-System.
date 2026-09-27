# Personal Finance Tracker

## Overview
This is a simple **terminal-based finance tool** written in Python. It lets multiple users create accounts to track their money. You can log your income (money earned) and expenses (money spent), see smart charts of your budget, and export everything to a spreadsheet.

## Features
* **Private Accounts:** Everyone can create their own username and password. Your data stays separate from other users.
* **Login Security:** Gives you 3 chances to enter the right password before locking you out to protect your data.
* **Easy Tracking:** Add transaction names, amounts, and categories (like Salary, Food, or Rent). If you skip entering a date, it automatically uses today's date.
* **Money Analytics:** Instantly calculates your total earnings, total spending, and remaining balance. It also tells you your highest spending category.
* **Excel Export:** Saves your transactions into a clean `.csv` file that you can open directly in Microsoft Excel.

## Technologies Used
* **Python 3:** The programming language used to build the tool.
* **Text Files (.txt):** Used like a simple database to remember user accounts and money history.

## How to Install & Run

### Prerequisites
Make sure you have Python installed on your computer. You can check by typing this in your terminal/command prompt:
```bash
python --version
```

### Step-by-Step Guide
1. **Save the file:** Save the code script as `finance_manager.py` on your computer.
2. **Open Terminal:** Open your terminal or command prompt and go to the folder where you saved the file.
3. **Run the program:** Type the following command and press Enter:
   ```bash
   python finance_manager.py
   ```

## How to Test It
To make sure everything works perfectly, try these quick steps:
1. **Create an Account:** Choose option `1` to register. Type a username and a strong password (at least 10 letters/numbers long, with at least 2 numbers).
2. **Log In:** Choose option `2` and log in with your new account.
3. **Add Money Records:** Choose option `1` in the dashboard to add an income or an expense. Try pressing Enter on the date to see it automatically fill in today's date.
4. **See your Balance:** Choose option `2` or `3` to see your money breakdowns and analytics.
5. **Create a Spreadsheet:** Choose option `4`. Check your folder for a new file named `[your_username]_financial_export.csv` and open it with Excel.


#### thank you $####