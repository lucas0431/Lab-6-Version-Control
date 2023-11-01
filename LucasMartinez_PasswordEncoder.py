# displays the menu for user to choose an option
def menu_display():
    print("Menu")
    print("-"*13)
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encoder(user_password):
    user_password = " "
    for i in range(len(user_password)):
        (str(int(user_password[i]+3)))

#
if __name__ == "__main__":
    menu_display()
    user_input = input("Please enter an option: ")
    while user_input != "3":
        if user_input == "1":
            user_password = input("Please enter your password to encode: ")
            encoded_password = encoder(user_password)
            print("Your password has been encoded and stored!")