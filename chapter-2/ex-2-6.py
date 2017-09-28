# Programming Exercise 2-6
#
# Program to calculate a total sale price using state and local sales tax.
# This program prompts a user for an amount of purchase,
# uses constants to calculate state, county and total sales tax, and a purchase total
# then displays the details of these calculations for the user.

# Variables for purchase amount, state tax, county tax, total tax and total sale
# all initialized as floats
purchase_price = float(0)
state_tax = float(0)
county_tax = float(0)
total_tax = float(0)
total_sale = float(0)
# Constants for the state and county tax rates
STATE_TAX_RATE = float(.06)
COUNTY_TAX_RATE = float(0)

# Get the amount of purchase from the user, casting it to a float.
purchase_price = float(input("How much is it?:   "))

# Calculate the state sales tax.
state_tax = purchase_price * STATE_TAX_RATE

# Calculate the county sales tax.
county_tax = purchase_price * COUNTY_TAX_RATE

# Sum the total tax.
total_tax = county_tax + state_tax

# Calculate the total of the sale.
total_sale = total_tax + purchase_price

# Print detailed information about the sale, formatting all values to two decimal places.
print("Total purchase:   ", purchase_price,"\nTotal tax:   ", total_tax,"\nTotal price:   ",total_sale )




