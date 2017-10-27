# Programming Exercise 6-1
#
# Program to display the contents of a text file.
# This program takes no user input, but requires a numbers.txt file,
# opens the fine and reads the whole contents at once,
# and displays the contents.


# define the main function
def main():
    
    file_name = ""
    file_contents = ""
    
    
    file_name_input = ""

    
    file_name_input = raw_input("EX:  numbers.txt\nEX:  workspace/exercises/chapter-6/numbers.txt\nEX:  ../chaptEnter the file you want to open and read:   ")

    
    file_name = open(file_name_input, 'r')
    # Open numbers.txt file for reading
    # that is, use a variable to hold the file handle created when opening the file


    # Read in data and store its contents
    file_contents = file_name.read()

    # Close file
    file_name.close()


    # Print the contents
    print(file_contents)

# Call the main function.
main()

