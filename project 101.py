from datetime import datetime 

## setting global names####
global username__, pasword__

username__ = ""
pasword__ = ""
financial_ledger = []
userdatabase = {}
userfiles = "userfiles.txt" 
entryfiles = ""


# detailes of useres
def save_user_details(newuser, newpasword):
    with open(userfiles, "a") as file:
        file.write(f"{newuser}|||{newpasword}\n")

def load_user_data():
    global userdatabase
    userdatabase = {}
    
    try:
        with open(userfiles, "r") as file:
            for line in file:
                clean = line.strip()
                if "|||" in clean:
                    parts = clean.split("|||")
                    if len(parts) == 2:
                        userdatabase[parts[0]] = parts[1]
    except FileNotFoundError:
        
        pass 


# finantial details
def save_financial_data():
    global entryfiles  
    with open(entryfiles, "w") as file:
        for entry in financial_ledger:
            line = f"{entry['name']}|||{entry['date']}|||{entry['amount']}|||{entry['record']}|||{entry['category']}\n"
            file.write(line)



def load_financial_data():
    global financial_ledger, entryfiles 
    financial_ledger = [] 
    
    try:
        with open(entryfiles, "r") as file:
            for line in file:
                cleaned = line.strip()
                if cleaned != "":
                    parts = cleaned.split("|||")
                    
                    if len(parts) == 5:
                        val = float(parts[2]) 
                        entry = {
                            "name": parts[0],
                            "date": parts[1],
                            "amount": val, 
                            "record": parts[3],
                            "category": parts[4]
                        }
                        financial_ledger.append(entry) 
                        
                    elif len(parts) == 4:
                        val = float(parts[2])
                        entry = {
                            "name": parts[0],
                            "date": parts[1],
                            "amount": val, 
                            "record": "loss",       
                            "category": "Other Expense"  
                        }
                        financial_ledger.append(entry) 
    except FileNotFoundError:
        pass



#creating new user 
def new_user_registration():
    print(" ------ New User Registration ------")
    load_user_data()

    while True:
        username = input("create a username unique to you:== ").strip()
        if username == "":
            print("username cannot be empty")
        elif username in userdatabase:
            print("another user already use this username, please try another one")
        else:
            break

    while True:
        pasword = input("create a unique pasword, pasword must be 10 characters long with minimum 2 numbers:==").strip()
        pasword_confirm = input("confirm your pasword:==")
        digit = sum(1 for char in pasword if char.isdigit())
        if len(pasword) < 10:
            print("pasword must be atleast 10 characters long")
        elif digit < 2:
            print("pasword must have atleast 2 numbers")
        elif pasword == "":
                   print("pasword cannot be empty")
        elif pasword != pasword_confirm:
                   print("pasword does not match, please try again")
        else:
            save_user_details(username, pasword)
            print("registration is successful, you can login now!")
            break


# user login with 3attempts
def user_login():
    global entryfiles, username__, pasword__  
    print(" ------ User Login page ------")
    load_user_data() 
    
    if len(userdatabase) == 0:
        print("No users found in the system. Please register first.")
        return False
        
    attempts = 0
    maxattempts_ = 3
    
    while attempts < maxattempts_:
        loginusername = input("enter your username:==").strip()
        loginpasword = input("enter your password:==").strip()
        
        if loginusername in userdatabase and loginpasword == userdatabase[loginusername]:
            print("login successful, access granted.")
            username__ = loginusername
            pasword__ = userdatabase[loginusername]
            entryfiles = f"{username__}_entryfiles.txt"
            load_financial_data()
            return True
        else:
            attempts += 1
            remainingattempts = maxattempts_ - attempts
            print(f"Invalid credentials. Attempts used: {attempts}/{maxattempts_}")
            if remainingattempts > 0:
                print(f"You have {remainingattempts} attempts left, please try again.")
                
    print("Too many failed tries. Access Denied. Returning to main menu")
    return False       


# export data to excel.
def exportdata_to_excel():
    if len(financial_ledger) == 0:
        print("No transactions available to export.")
        return
        
    exportfilename = f"{username__}_financial_export.csv"
    
    with open(exportfilename, "w") as file:
        
        file.write("entry Name,Date,Classification,Category,Amount\n")
        
        for entry in financial_ledger:
            name = f'"{entry["name"]}"' 
            date = entry["date"]
            record = entry["record"]
            category = entry["category"]
            amount = entry["amount"]
            
           
            line = f"{name},{date},{record},{category},{amount}\n"
            file.write(line)
            
    print(f"Success! Your Data has been exported to '{exportfilename}'.")
    print("You can open this file as a exel file")


def financial_manager_entry():
    print("----- add financial entry -----")

    
    while True:
        name = input("enter the name of the financial entry:==").strip()
        if "|||" in name:
            print("The entry name cannot contain '|||' characters.")
            continue
        break

        
    while True:
        print("Enter the date (dd/mm/yyyy) or press [ENTER] to use today's date.")
        date_input = input("Date:==").strip()

        
        if date_input == "":
            date = datetime.now().strftime("%d/%m/%Y")
            print(f"-> Automatically stamped with today's date: {date}")
            break
        else:
            try:
                datetime.strptime(date_input, "%d/%m/%Y")
                date = date_input
                break
            except ValueError:
                print("Invalid format/date values! Please match 'dd/mm/yyyy' format rules exactly.")


    while True:
        try:
            amount = float(input("enter the amount of the financial entry:=="))
            if amount <= 0:
                print("enter a valid amount greater than 0")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a right value for the amount.")


    while True:
        print(" ----------------------------------------------")
        print("                TRANSACTION TYPE              ")
        print(" ----------------------------------------------")
        print("     1.      gain ( income or revenue )           ")
        print("     2.      loss ( expense or cost )              ")
        print(" ----------------------------------------------")
        transactiontype = input("select classification option (1 or 2):==")


        if transactiontype == "1":
            record = "gain"

            
            print(" ----------------------------------------------")
            print("                SELECT GAIN CATEGORY            ")
            print(" ----------------------------------------------")
            print("     1. Salary")
            print("     2. Side Hustle")
            print("     3. Investments")
            print("     4. Gifts")
            print("     5. Other Income")
            print(" ----------------------------------------------")
            
            cat_choice = input("Select a category (1-5):==").strip()
            if cat_choice == "1":
                category = "Salary"
            elif cat_choice == "2":
                category = "side Hustle"
            elif cat_choice == "3":
                category = "Investment"
            elif cat_choice == "4":
                category = "Gift"
            elif cat_choice == "5":
                category = "Other"
            else:
                print("Invalid category choice. Defaulting to 'Other Income'.")
                category = "Other"
            break

            
        elif transactiontype == "2":
            record = "loss"
            

            
            print(" ----------------------------------------------")
            print("                SELECT LOSS CATEGORY            ")
            print(" ----------------------------------------------")
            print("     1. Food ")
            print("     2. Rent ")
            print("     3. Entertainment")
            print("     4. Transportation")
            print("     5. Other Expense")
            print(" ----------------------------------------------")
            
            loss_choice = input("Select a category (1-5):==").strip()
            if loss_choice == "1":
                category = "Food"
            elif loss_choice == "2":
                category = "Rent"
            elif loss_choice == "3":
                category = "Entertainment"
            elif loss_choice == "4":
                category = "Transport"
            elif loss_choice == "5":
                category = "Other Expense"
            else:
                print("Invalid category choice. Defaulting to 'Other Expense'.")
                category = "Other Expense"
            break
        else:
            print("Invalid choice. Please select option 1 or 2.")


    new_entry = {
        "name": name,
        "date": date,
        "amount": amount,
        "record": record,
        "category": category  
    }
    return new_entry



#finantial record

def view_financial_record():
    print("---  Account Activity record ---")
    if len(financial_ledger) == 0:
        print("No transaction logged yet.")
        return

  
    print(f"{'Name':<15} | {'Date':<12} | {'Category':<15} | {'Type':<6} | {'Amount'}")
    print("-" * 65) 
    
    total_gains = 0.0
    total_losses = 0.0
    
    for entry in financial_ledger:
        if entry["record"] == "gain":
            marker = "+"
            total_gains += entry["amount"]
        else:
            marker = "-"
            total_losses += entry["amount"]
            
       
        print(f"{entry['name']:<15} | {entry['date']:<12} | {entry['category']:<15} | {entry['record']:<6} | {marker}${entry['amount']:,.2f}")
    
    net_balance = total_gains - total_losses

    print("------------------------------------------------------")
    print(f"Total gains  : +${total_gains:,.2f}")
    print(f"Total Losses : -${total_losses:,.2f}")
    print(f"Net Balance  : ${net_balance:,.2f}")
    print("------------------------------------------------------")


# financial dashboard menu
def finance_dashboard_menu():
    while True:
        print("==============================")
        print(f"   FINANCE DASHBOARD: {username__}   ")
        print("==============================")
        print("1. Add New Transaction Record")
        print("2. View Ledger Activity Logs")
        print("3. View Category Analytics ")  
        print("4. Export Ledger to Excel Sheet")
        print("5. Log Out / Exit System")
        
        choice = input("Select an action (1-5): ").strip() 
        
        if choice == "1":
            while True:
                new_entry = financial_manager_entry()
                financial_ledger.append(new_entry)
                save_financial_data()
                print("Financial entry added successfully!")
              
                repeat = input("Do you want to add another entry? (y/n): ").strip().lower()
                if repeat != "y":
                    print("Returning to dashboard menu.")
                    break

        elif choice == "2": 
            view_financial_record()
        elif choice == "3":                     
            financial_analytics()
        elif choice == "4":                    
            exportdata_to_excel()
        elif choice == "5":                   
            print("Safely logging out of your session. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")


#analysis of data
def financial_analytics():

    print("--- Financial Analytics Dashboard ---")

    if len(financial_ledger) == 0:
        print("No data available to analyze yet. Add transactions first!")
        return

   
    gain_categories = {}
    loss_categories = {}

    for entry in financial_ledger:

        cat = entry["category"]
        amount = entry["amount"]
        
        if entry["record"] == "gain":
            gain_categories[cat] = gain_categories.get(cat, 0.0) + amount
        else:
            loss_categories[cat] = loss_categories.get(cat, 0.0) + amount

    print("==============================================")
    print("               INCOME ANALYSIS                ")
    print("==============================================")

    if gain_categories:
        
        top_gain_cat = max(gain_categories, key=gain_categories.get)
        print(f"Highest Earning Category: {top_gain_cat}")
        print(f"Total Amount Earned   : ${gain_categories[top_gain_cat]:,.2f}")
        
        print("All Income Breakdowns:")
        for cat, total in sorted(gain_categories.items(), key=lambda x: x[1], reverse=True):
            print(f" - {cat:<15}: ${total:,.2f}")

     


    else:
        print("No income logs found.")


    print("==============================================")
    print("               EXPENSE ANALYSIS               ")
    print("==============================================")
    if loss_categories:


        
        top_loss_cat = max(loss_categories, key=loss_categories.get)
        print(f" Highest Spending Category: {top_loss_cat}")
        print(f" Total Amount Spent      : ${loss_categories[top_loss_cat]:,.2f}")
        
        print("All Expense Breakdowns:")
        for cat, total in sorted(loss_categories.items(), key=lambda x: x[1], reverse=True):
            print(f" - {cat:<15}: ${total:,.2f}")
    else:

        print("No expense found.")
        print("==============================================")





# main loop
load_user_data()                

logged_in = False
while True:
    print("==============================")
    print("    LOGIN AND SIGNUP IN SYSTEM   ")
    print("==============================")
    print("1. Register New Account")
    print("2. Login to Dashboard")
    print("3. Exit Program")
    mainchoice = input("Select an option (1-3): ").strip()
        
    if mainchoice == "1":
        new_user_registration()
    elif mainchoice == "2":
        logged_in = user_login() 
        if logged_in:
            print("Logged in successfully.")
            finance_dashboard_menu()
            logged_in = False 
    elif mainchoice == "3":
        print("Program ended safely. Goodbye!")
        break
    else:
        print("Invalid choice. Please select option 1, 2, or 3.")


