# Programming Exercise 3-6
#
# Program to check if a date is 'magic' (day * month = year).
# This program takes a month, day and year from the user as integers,
# Checks to see if each is in range, then checks whether month * day = year,
# then displays an appropriate message depending on the result

# Variables for month, day, year and message
# initialize month, day and year as integers, message as a string
month = int(0)
day = int(0)
year = int(0)

# Get month and cast it to int
month = int(input("enter month   "))

# Get day and cast it to int
day = int(input("enter day   "))

# Get year and cast it to int
year = int(input("enter year in ##"))

# This problem can be solved with if-else logic by the reducing the problem domain
# if month input is out of range
if month < 1 or month > 12:
	# set message to hold "invalid month" message
    message = "invalid month"

# else if day input is out of range
elif day < 1 or day > 31:
    # set message to hold "invalid day" message
    message = "invalid day"
# else if  year input is out of range (greater than 99 or less than 0)
elif year < 0 or year > 99:
    # set message to hold "invalid year" message
    message = "invalid year"
# else 
else:
    # set message to hold the date in 00/00/00 form
    message = month + "/"+day+"/"+year
    # if day * month equals year, add " is a magic date" to message
    if year == day * month:
        message += " is a magic date."
    # else add " is not a magic date" to message
    else:
        message += " is not a magic date."
# print message for the user
print(message)

