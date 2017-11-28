#asks user to enter valid number between 1-100




def main():
    
    ErrorFree = False
    valid_number = False
    
    while not valid_number:
        ErrorFree = False
        valid_number = False
    
        while not ErrorFree:
        
            user_input = ""
            user_input = input("enter a number between 1-100:   ")
    
            try:
                user_input = float(user_input)
                ErrorFree = True
            except ValueError as n:
                print("Your entered an invalid number:   ",n )
            
        if user_input >= 1 and user_input<=100:
            print("Your value ,",user_input,", was acceptable.")
            valid_number = True
        else:
            print("Your value, ",user_input,", was unaccepted")
    
    
    
    
    
    
    
main()