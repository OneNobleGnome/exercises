# Programming Exercise 3-3
#
# Program to assign an age category to an numerical age.
# This program will prompt the user for an integer age value,
# and use it to choose an age category,
# then display that category on the screen.

# Variables to hold an age and a category.
# initialize age as an int and category as a string.
age = int(0)
category = str()
# Get the person's age.
# remember to convert the input to an int
age = int(input("What is the persons age?   "))

# Determine if the person is an infant, child, teenager, or adult and set the category.
# Use a series of if ... elif ... etc. statements.
if age <= 3:
    category = "infant"
elif age <= 12:
    category = "child"
elif age <18:
    category = "teenager"
else:
    category = "adult"



# display a message with the age category.
print("The subject is", age,", and is a", category)


