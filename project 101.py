# creating the usere sineup
global username__, pasword__
username__=""
pasword__=""

def new_user_registration():
    print(" ------ New User Registration ------")

    while True:
        username = input("create a username unique to you:== ")
        if username == username__:
            print("another user already use this username, please try another one")
            if username=="":
                print("username cannot be empty")
            else:
                break

    while True:
        pasword = input("create a unique pasword , pasword must be 10 characteers long with atleast 2 numbers:==")
        pasword_confirm = input("confirm your pasword:==")
        if len(pasword) < 10:
            print("pasword must be atleast 10 characters long")
        elif pasword == sum(1 for char in pasword if char.isdigit()):
            if pasword < 2:
                print("pasword must have atleast 2 numbers")
                if pasword == "":
                    print("pasword cannot be empty")
                else:
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
                return

logged_in = False
while True:
    print("1. New User Registration")
    print("2. User Login")
    choice = input("Enter your choice 1 or 2:== ")
    if choice == "1":
        new_user_registration()
    elif choice == "2":
        logged_in = user_login()
    else:
        print("Invalid choice, please try again.")
