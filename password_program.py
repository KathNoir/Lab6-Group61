
# Program and encode function by Katherine Blanco

# Defines the function to encode a password
def encode(password, enc_pass=""):

    # For each number in password, increase it by 3
    # If the number is between 7 and 9, only get the number in the tenth place (10) -> (0)
    for i in password:
        if int(i) < 7:
            enc_pass += str(int(i) + 3)
        elif 7 <= int(i) <= 9:
            enc_pass += str((int(i) + 3) % 10)

    print("Your password has been encoded and stored!\n")
    return enc_pass

#### Add decode function here
#### Add decode function here

def main():

    encodedPassword = ""

    # Repeats the program until user selects 3
    while True:
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit\n")

        option = int(input("Please enter an option: "))

        # Selects the encode option
        if option == 1:
            password = input("Please enter your password to encode: ")
            if len(password) == 8:
                encodedPassword = encode(password)
            else:
                print("Your password isn't long enough. Try again.")

        ##### Add decode function here
        # # Selects the decode option
        # elif option == 2:
        #     if encodedPassword != "":
        #
        #     else:
        #         print("You must encode a password first.\n")

        # Quits the program
        elif option == 3:
            break

        # Makes it so the user can only choose 1, 2, or 3
        else:
            print("Not a valid option. Try again.\n")


# Runs the program
if __name__ == "__main__":
    main()