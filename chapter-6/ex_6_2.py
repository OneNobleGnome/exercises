# Programming Exercise 6-2
#
# Program to read up to five lines of a file and display them.
# This program prompts the user for a file name,
# attempts to open and read five lines of the file,
# then displays those lines and finally closes the file.



# define a main function
def main():

    # Declare local variables, line and filename as strings and counter as int
    line = ""
    file_name = ""
    file_name_input = ""
    
    
    # Prompt the user for a file name
    file_name_input = raw_input("EX:  numbers.txt\nEX:  workspace/exercises/chapter-6/numbers.txt\nEX:  ../chaptEnter the file you want to open and read:   ")

    # Open the specified file for reading
    file_name = open(file_name_input, 'r')
    
    # Read the first line of the file and increment the line counter to 1
    # this is needed to prepare conditions for the while loop to follow
    line = file_name.readline()
    line_counter = 1
    
    #print(line)
    # Use a while loop to read until counter is 5 or reading produces no data
    while line_counter < 5 and line != "":
	# remove carriage returns before display, as print() supplies its own
        line = line.rstrip()
        # print the current line
        print(line)
        # read the next line
        line = file_name.readline()
        # Update counter when line is read
        line_counter += 1

    # Close file
    file_name.close()

# Call the main function to begin the program

main()
