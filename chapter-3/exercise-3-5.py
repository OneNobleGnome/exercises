# Programming Exercise 3-5
#
# Program to convert a value in kilograms to Newtons, then check whether it is in range.
# This program will prompt a user for a mass in kilograms,
# convert it to Newtons and use constants to check if the weight is within range,
# then display the weight and a range message.



# Global constants for minimum, maximum and mass multiplier values
MIN_MASS = 9.81
MAX_MASS = 10.00
MASS_MULTI = 9.81

# Variables for weight and mass initialized as floats   
weight = float(0)
mass = float(0)

# Get mass from user and convert it to a float
mass = float(input("Enter Mass"))

# Calculate weight using the mass multiplier constant
weight = mass * MASS_MULTI

# Display the weight
print("weight")
# If weight > maximum or < than minimum display an appropriate message
if weight>MAX_MASS or weight<MIN_MASS:
    print("weight is less than min mass or greater than max")







