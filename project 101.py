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

    choice = input("Select an option (1-3): ").strip() 
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
   