# Programming Exercise 5-3
#
# Program to compute recommended insurance to carry on an item.
# This program accepts a replacement cost from a user,
# calculates a minimum recommended insurance to carry from a global constant,
# then passes these values to a function to be displayed



# Global constant for the percent of replacement cost to insure

PERCENT_OF_REPLACEMENT = float(0.20)

# Define the main function
def main():
    # Define local float variables for replacement cost and minimum insurance
    replacement_cost = float()
    minimum_insurance = float()
    # Get the replacement cost from the user
    replacement_cost = float(input("What is the replacement cost:   "))
    # Calculate the minimum insurance amount using the global constant
    minimum_insurance = PERCENT_OF_REPLACEMENT * replacement_cost
    # Call the function to display the insurance details, 
    # passing the replacement cost and minimum insurance to the function
    insurance_details(replacement_cost, minimum_insurance)

      
# Define a function to display the insurance details
# This function accepts the replacement cost and minimum insurance as parameters,
# uses the global constant to calculate percent insured,
# and displays the insurance details.
def insurance_details(replacement_cost, minimum_insurance):
	# display the replacement cost, formatting the value to 2 decimal places
    print("Your replacement cost is ", format(replacement_cost,'.2f'))
    # display the percent insured, formatting the value to 2 decimal places
    print("Your % insured needs to be ", (str(PERCENT_OF_REPLACEMENT * 100) +"%"))
	# display the minimum insurance, formatting the value to 2 decimal places
    print("Your minimum insurance is ", format(minimum_insurance,'.2f'))


# Call the main function to start the program
main()
