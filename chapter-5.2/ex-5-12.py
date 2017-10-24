# Programming Exercise 5-12
#
# Program to find the greater of two integers.
# This program accepts two integers,
# passes them to a function that compares them,
# and displays which one is greater.



# define the main function
def main():
    # Define local variables to hold two integers
    int_1 = 0
    int_2 = 0
    # prompt the user for the first integer
    int_1 = int(input("Enter the first int:   "))
    
    # prompt the user for the second integer
    int_2 = int(input("Enter second int:   "))

    # print the return value from calling a function to find the greater of two integers
    # the two integers are passed as arguments
    if int_1 != int_2:
        greater_int = greater(int_1, int_2)
        print(greater_int, " is greater")
    else:
        print("Both are equal")
# Define a function to compare integer values.
# This function accepts two integer parameters,
# compares them,
# and returns the value of the greater.
def greater(int_1, int_2):
	# if the first integer is greater, return the first integer
    if int_1 > int_2:
        return(int_1)
	# else, return the second integer
    elif int_1 < int_2:
        return(int_2)
    else:
        return ("both numbers are equal")


# Call the main function to start the program
main()




