# Programming Exercise 5-2
#
# Program to calculate final purchase details.
# This program takes a purchase amount from a user,
# then calculates state tax, county tax and total tax,
# 	and passes them to a function to be totaled
# and displayed



# Global constants for the state and county tax rates
STATE_TAX_RATE = 0.07
COUNTY_TAX_RATE = 0.00


# define the main function
def main():
    # Define local float variables for purchase, state tax and county tax
    purchase_amt = float()
    state_tax_amt = float()
    county_tax_amt = float()
    # Get the purchase amount from the user
    purchase_amt = float(input("Insert the purchase amount here:   "))
    # Calculate the state tax using the global constant for state tax rate
    state_tax_amt = purchase_amt * STATE_TAX_RATE
    # Calculate the county tax using the global constant for county tax rate
    county_tax_amt = purchase_amt * COUNTY_TAX_RATE
    # Call the sale details function, passing the purchase, state tax and county tax
    sale_details(purchase_amt,state_tax_amt,county_tax_amt)


# define a function to display purchase details
# this function accepts purchase, stateTax, and countyTax as arguments,
# calculates the total tax and sale total,
# then displays the purchase details
def sale_details(purchase_amt,state_tax_amt,county_tax_amt):
    # Define local float variables for total tax and sale total
    total_tax = float()
    sale_total = float()
	# Calculate the total tax
    total_tax = state_tax_amt + county_tax_amt
	# Calculate the total sale
    sale_total = total_tax + purchase_amt
    # Display the purchase details, including purchase, state tax, county tax,
    #	total tax, and sale total, each on a line.  Format floats to 2 decimal places.
    purchase_amt = float(format(purchase_amt,'.2f'))
    state_tax_amt = float(format(state_tax_amt,'.2f'))
    county_tax_amt = float(format(county_tax_amt,'.2f'))
    total_tax = float(format(total_tax,'.2f'))
    sale_total = float(format(sale_total,'.2f'))
    
    print("Your purchase was:   ",purchase_amt,
    "\nYour state tax was:   ",state_tax_amt,
    "\nYour county tax was:   ",county_tax_amt,
    "\nYour total tax was:   ",total_tax,
    "\nYour total price is:   ",sale_total)

# Call the main function to start the program.
main()
