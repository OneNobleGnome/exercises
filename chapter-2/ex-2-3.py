# Programming Exercise 2-3
#
# Program to convert area in square feet to acres.
# This program will prompt a user for the size of a tract in square feet,
# then use a constant ratio value to calculate it value in acres
# and display the result to the user.

# Variables to hold the size of the tract and number of acres.
# be sure to initialize these as floats


# Constant for the number of square feet in an acre
ACRES_IN_FT = 43560

# Get the square feet in the tract from the user
# you will need to convert this input to a float

feet_sq = float(input("how many square feet are there?   "))


# Calculate the number of acres.
acres = ACRES_IN_FT * feet_sq

# Print the number of acres.
# remember to format the acres to two decimal places
print("{0:.2f}".format(acres))




