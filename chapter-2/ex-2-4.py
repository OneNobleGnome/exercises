# Programming Exercise 2-4
#
# Program to compute a final price for five items with tax.
# This program will prompt a user for a set of five prices,
# sum them to a subtotal and calculate sales tax with tax rate stored in a constant,
# then display the results on the screen.

# Variables to hold the prices of five items, the subtotal, and the total.
# All should be initialized as floats.
candy =  0
video_game = 0
snacks = 0
phone = 0
toy = 0
sub_total = 0
total = 0
sales_tax_total = 0
# Constant for the sales tax rate.
sales_tax = .07

# Get the price of each item by prompting the user.
# You will need to convert each input to a float.
candy = float(input("what is the price, candy?:   "))
video_game = float(input("what is the price, video_game?:   "))
snacks = float(input("what is the price, snacks?:   "))
phone = float(input("what is the price, phone?:   "))
toy = float(input("what is the price, toy?:   "))

# Calculate the subtotal by adding up the item prices.
sub_total = candy + video_game + snacks + phone + toy

# Calculate the sales tax by multiplying the subtotal by the tax rate.
sales_tax_total = sales_tax * sub_total

# Calculate the total by adding the subtotal and tax.
total = sales_tax_total + sub_total

# Print the values for the subtotal, tax and total.
# Label each value, and format them to display with two decimal places. 

print("Your sub-total is", ("{0:.2f}".format(sub_total)),"the total tax is", ("{0:.2f}".format(sales_tax_total)),"and your total is ", ("{0:.2f}".format(total)))



