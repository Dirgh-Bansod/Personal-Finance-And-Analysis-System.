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
    userdatabase={}
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
    with open(entryfiles, "w") as file:
        for entry in financial_ledger:
            line = f"{entry['name']}|||{entry['date']}|||{entry['ammount']}|||{entry['record']}\n"
            file.write(line)

def load_financial_data():
    global financial_ledger
    financial_ledger = [] 
    
    try:
        with open(entryfiles, "r") as file:
            for line in file:
                cleaned = line.strip()
                if cleaned != "":
                    parts = cleaned.split("|||")
                    if len(parts) == 4:
                        val = float(parts[2]) 
                        entry = {
                            "name": parts[0],
                            "date": parts[1],
                            "ammount": val, 
                            "record": parts[3]
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
        elif username == userdatabase:
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

#financial dashboard menu
def finance_dashboard_menu():
    while True:
        print("==============================")
        print(f"   FINANCE DASHBOARD: {username__}   ")
        print("==============================")
        print("1. Add New Transaction Record")
        print("2. View Ledger Activity Logs")
        print("3. Log Out / Exit System")
        
        choice = input("Select an action (1-3): ").strip()
        
        if choice == "1":
            new_entry = financial_manager_entry()
            financial_ledger.append(new_entry)
            save_financial_data()
            print(f"financial entry added successfully as {new_entry}")
            print("-----------------------------------------")
            repeat = input("Do you want to add another entry? (y/n): ").strip().lower()
            if repeat != "y":
                print("Returning dashbord menu.")   
        elif choice == "2":
            view_financial_record()
        elif choice == "3":
            print("Safely logging out of your session. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# financial manager entry setup
def financial_manager_entry():
    print("----- add finantial entry -----")
    name = input("enter the name of the financial entry:==")
    date = input("enter the date of the financial entry (dd/mm/yyyy):==")
    while True:
        try:
            ammount = float(input("enter the ammount of the financial entry:=="))
            if ammount <= 0:
                print("enter a valid ammount greater than 0")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a right value for the ammount.")
            
    while True:
        print(" ----------------------------------------------")
        print("                TRANSACTION TYPE               ")
        print(" ----------------------------------------------")
        print("     1.      gain ( income or revenue )           ")
        print("     2.      loss ( expense or cost )              ")
        print(" ----------------------------------------------")
        transaction_type = input("select classification option (1 or 2):==")
        if transaction_type == "1":
            record = "gain"
            break
        elif transaction_type == "2":
            record = "loss"
            break
        else:
            print("Invalid choice. Please select option 1 or 2.")

    new_entry = {
        "name": name,
        "date": date,
        "ammount": ammount,
        "record": record
    }
    return new_entry

#finantial record and total sumation
def view_financial_record():
    print("---  Account Activity record ---")
    if len(financial_ledger) == 0:
        print("No transaction logged yet.")
        return
        
    print(f"{'Name':<15} | {'Date':<12} | {'Type':<6} | {'Amount'}")
    print("-" * 50)
    
    total_gains = 0.0
    total_losses = 0.0
    
    for entry in financial_ledger:
        if entry["record"] == "gain":
            marker = "+"
            total_gains += entry["ammount"]
        else:
            marker = "-"
            total_losses += entry["ammount"]
            
        print(f"{entry['name']:<15} | {entry['date']:<12} | {entry['record']:<6} | {marker}${entry['ammount']:,.2f}")
    
    net_balance = total_gains - total_losses
    
    print("----------------------------------------")
    print(f"Total gains  : +${total_gains:,.2f}")
    print(f"Total Losses : -${total_losses:,.2f}")
    print(f"Net Balance  : ${net_balance:,.2f}")
    print("----------------------------------------")




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
    choice = input("Select an option (1-3): ")
        
    if choice == "1":
        new_user_registration()
    elif choice == "2":
        logged_in = user_login()
        if logged_in:
            print("logged in successfully.")
            load_financial_data()
            finance_dashboard_menu()
    elif choice == "3":
        print("Program ended.")
        break
    else:
        print("Invalid choice. Please select option 1, 2, or 3.")
