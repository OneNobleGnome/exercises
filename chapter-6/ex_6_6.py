# Programming Exercise 6-6
#
# Program to find the average value of numbers stored in a text file.
# This program takes no user input but requires a file with one number per line,
# which it opens, loops through totaling the values, then averages them,
# and displays the average value on the screen.

# Define the main function
def main():
    # Declare local float variables for number and total, and an integer counter
    number = 0.0
    total = 0.0
    counter = 0
    # Open numbers.txt file for reading
    f = open('numbers.txt', 'r')
    # Iterate over the lines in the file
    for line in f.readlines():
        # increment the counter
        counter += 1
        # get a number from the current line
        number = float(line)
        # add the number to the total
        total += number
        
    # Close file
    f.close()

    # Calculate average
    average = total/counter
    
    # Display the average of the numbers in the file
    print("Your average is... ",average)


# Call the main function to start the program
main()

