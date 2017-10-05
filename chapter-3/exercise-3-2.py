# Programming Exercise 3-2
#
# Program to find which of two rectangles has the greater area.
# This program will get two sets of lengths and widths from a user,
# use them to calculate and compare two area values,
# and display a message comparing those areas

# Local variables
# you need length, width and area for A and for B
# initialize these as floats
a_length = float(0)
a_width = float(0)
a_area = float(0)
b_length = float(0)
b_width = float(0)
b_area = float(0)
# Get length A from the user and convert it to a float
a_length = float(input("What is the length of rectangle A?   "))

# Get width A from the user and convert it to a float
a_width = float(input("What is the width of rectangle A?   "))

# Get length B from the user and convert it to a float
b_length = float(input("What is the length of rectangle B?   "))

# Get width B from the user and convert it to a float
b_length = float(input("What is the length of rectangle B?   "))

# Calculate area A
a_area = a_length * a_width

# Calculate area B
b_area = b_length * b_width

# Print each area, formatting the values to 2 decimal places
print("Area of A =", a_area,"\nArea of B =", b_area)
# if area A is greater, print "A is greater" message.
if a_area > b_area:
    print("Area of A is greater than B")
# else if area B is greater, print "B is greater" message.
elif b_area > a_area:
    print("Area of B is greater than A")
# else print "A and B are equal" message.
else:
    print("The area of A & B are equal")
