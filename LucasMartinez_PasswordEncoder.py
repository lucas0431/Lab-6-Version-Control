# displays the menu for user to choose an option
def menu_display():
    print("Menu")
    print("-"*13)
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encoder(password_1):
    e_password = ""
    for i in range(len(password_1)):
        e_password += (str((int(password_1[i])) + 3))
    return e_password


def decoder(password):
    d_password = ''
    for i in range(len(password)):
        d_password += (str((int(password[i])) - 3))
    return d_password


#
if __name__ == "__main__":
    menu_display()
    user_input = input("Please enter an option: ")
    while user_input != "3":
        if user_input == "1":
            user_password = input("Please enter your password to encode: ")
            encoded_password = encoder(user_password)
            print("Your password has been encoded and stored!")
        elif user_input == "2":
            decoded_password = decoder(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
        menu_display()
        user_input = input("Please enter an option: ")
