# creating the usere login and sinup
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
        elif nuymber = sum(1 for char in pasword if char.isdigit()):
            if nuymber < 2:
                print("pasword must have atleast 2 numbers")
                if pasword == "":
                    print("pasword cannot be empty")
                elif:
                     break
                