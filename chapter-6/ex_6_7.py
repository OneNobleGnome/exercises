def main():
    valid_number = False

    while not valid_number:
        user_input = ""
        user_input = input("Please enter a number:   ")
        try:
            int(user_input)
            valid_number = True    # u can use either this line
        except ValueError:
            print(user_input, " was not a valid number.")
        else:
            valid_number = True    # or this line to set variable to true
            
    print("Your value was accepted")
main()