# Programming Exercise 3-1
#
# Program to display the name of a week day from its number.
# This program prompts a user for the number (1 to 7)
# and uses it to choose the name of a weekday
# to display on the screen.

# Variables to hold the day of the week and the name of the day.
# Be sure to initialize the day of the week to an int and the name as a string.
day_num = int(0)
day = str("day")
# Get the number for the day of the week.
# be sure to format the input as an int
day_num = int(input("what day is it(ex. sunday =1 monday = 2...)?:   "))

# Determine the value to assign to the day of the week.
# use a set of if ... elif ... etc. statements to test the day of the week value.
if day_num == 1:
    day = "Sunday"
elif day_num == 2:
    day = "Monday"
elif day_num == 3:
    day = "Tuesday"
elif day_num == 4:
    day = "Wednesday"
elif day_num == 5:
    day = "Thursday"
elif day_num == 6:
    day = "Friday"
elif day_num == 7:
    day = "Saturday"
# use the final else to display an error message if the number is out of range.
else:
    print("Number is out of range")

# display the name of the day on the screen.
print("The day is ",day)



