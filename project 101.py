# creating the usere sineup and login
global username__, pasword__
username__=""
pasword__=""

def new_user_registration():
    global username__, pasword__
    print(" ------ New User Registration ------")

    while True:
        username = input("create a username unique to you:== ")
        if username=="":
                print("username cannot be empty")
        elif username == username__:
            print("another user already use this username, please try another one")
        else:
            username__ = username
            break

    while True:
        pasword = input("create a unique pasword , pasword must be 10 characteers long with atleast 2 numbers:==")
        pasword_confirm = input("confirm your pasword:==")
        digit = sum(1 for char in pasword if char.isdigit())
        if len(pasword) < 10:
            print("pasword must be atleast 10 characters long")
        elif  digit < 2:
                print("pasword must have atleast 2 numbers")
        elif pasword == "":
                    print("pasword cannot be empty")
        elif pasword != pasword_confirm:
            print("pasword does not match, please try again")
        else:
            pasword__ = pasword
            print("registration is successfull, you can login now:  ")
            break



def user_login():
    print(" ------ User Login page ------")
    if username__ == "":
        print("No user found, please register first or enter a valid user name")
        return False
    while True:
            inputusername = input("enter your username:==")
            inputpasword = input("enter your pasword:==")
            if inputusername == username__ and inputpasword == pasword__:
               print("login successful, access granter,  ")
               print(f"welcome to the program {username__}")
               return True
            else:
                print("wrong username or password, please try again")
                

logged_in = False
loop_safety=0
while True:
    print("==============================")
    print("    LOGIN AND SIGNUP IN SYSTEM   ")
    print("==============================")
    print("1. Register New Account")
    print("2. Login to Dashboard")
    print("3. Exit Program")

    choice = input("Select an option (1-3): ")
    if loop_safety =="":
        print("Too many invalid attempts. Exiting program.")
        
    if choice == "1":
        new_user_registration()
    elif choice == "2":
        logged_in = user_login()
        if logged_in:
            print("logged in successfully.")
            break 
    elif choice == "3":
        print("Program ended.")
        break
    else:
        print("Invalid choice. Please select option 1, 2, or 3.")
        input("please select a valid option to continue:==")





# financial manager
def financial_manager_entry():
    print(" ----- add finantial entry -----")
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
        print("     1.      gain (income or revenue )           ")
        print("     2.      loss (expense or cost)              ")
        print(" ----------------------------------------------")
        transaction_type = input("select clacificaation option (1 or 2):==")
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
new_entry = financial_manager_entry()
print(f"financial entry added successfully as {new_entry}")
def view_financial_ledger():
    """Iterates through and prints all stored logs cleanly using a for loop."""
    print("---  Account Activity Ledger ---")
    if len(financial_manager_entry) == 0:
        print("No transaction entries logged yet.")
        return
        
    print(f"{'Name':<15} | {'Date':<12} | {'Type':<6} | {'Amount'}")
    print("-" * 50)
    
    for entry in financial_manager_entry:
        if entry["type"] == "Gain":
            marker = "+"
        else:
            marker = "-"
        print(f"{entry['name']:<15} | {entry['date']:<12} | {entry['type']:<6} | {marker}${entry['amount']:,.2f}")


def finance_dashboard_menu():
    """The post-login dashboard built with a continuous while loop."""
    while True:
        print("==============================")
        print(f"   FINANCE DASHBOARD: {username__}   ")
        print("==============================")
        print("1. Add New Transaction Record")
        print("2. View Ledger Activity Logs")
        print("3. Log Out / Exit System")
        
        choice = input("\nSelect an action (1-3): ").strip()
        
        if choice == "1":
            new_entry = financial_manager_entry()
            financial_manager_entry.append(new_entry)
        elif choice == "2":
            view_financial_ledger()
        elif choice == "3":
            print("Safely logging out of your session. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")