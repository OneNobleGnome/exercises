# Programming Exercise 2-2
#
# Program to compute expected profit from sales.
# This program will prompt a user for a sales projection
# and use it to calculate expected profit from a predefined profit margin
# then display the result.

# Variables to hold the sales total and the profit
# initialize them as float values
sales_total = float()
profit = float()
# Get the amount of projected sales.
# be sure to convert the input to a float
projected_sales = float(input("What is the sales total:   "))


# Calculate the projected profit using a 23% profit margin.
projected_profit = float(projected_sales * .23)

# Print the projected profit.
# be sure to format the output to two decimal places
print(round(projected_profit,2))




