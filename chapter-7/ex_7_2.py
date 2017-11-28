# Programming Exercise 7-2
#
# Program to display a list of random integers.
# This program takes no input,
# it loops through a list of integers and exchanges them for random integers,
# then displays the list on a single line.



# to use the random functions, import the random module
import random


# Define the main function
def main():
    # Initialize a list of integers.
    list_int = [0,0,0,0]

    # loop through the list
    for i in range(len(list_int)):
         # assigning a random integer to each member of the list
        list_int[i] = random.randint(0,10)
    # loop through the list
    for i in range(len(list_int)):

        # display the current value
        print(list_int[i])
        
        # add a comma and space, unless this is the last value
        if i < len(list_int):
            print(", ")

# Call the main function.


main()