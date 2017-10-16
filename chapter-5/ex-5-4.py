# Programming Exercise 5-4
#
# Program to compute monthly and annual auto expenses.
# This program prompts a user for several auto monthly expense amounts,
# then passes them to a function to total the values, annualize them,
# and display the details and totals on the screen.



# define the main function
def main():
    # Define local float variables for loan, insurance, gas, oil, tires and maintenance
    loan = float()
    insurance = float()
    gas = float()
    oil = float()
    tires = float()
    maintenance = float()
    # Get the amount of the monthly loan payment from the user.
    loan = float(input("What is your monthly loan payment:   "))
    
    # Get the amount of the monthly insurance from the user.
    insurance = float(input("What is your monthly insurance payment:   "))

    # Get the amount of the monthly gas from the user.
    gas = float(input("What is your monthly gas payment:   "))

    # Get the amount of the monthly oil from the user.
    oil = float(input("What is your monthly oil payment:   "))

    # Get the amount for monthly tire wear from the users.
    tires = float(input("What is your monthly tire payment:   "))

    # Get the amount for monthly maintenance from the user.
    maintenance = float(input("What is your monthly maintenance payment:   "))
        
    # Call the function to summarize car expenses,
    # passing the loan, insurance, gas, oil, tires and maintenance as arguments.
    sum_car_expenses(loan, insurance, gas, oil, tires, maintenance)
    


# Define a function to summarize car expenses,
# it accepts loan, insurance, gas, oil, tires, and maintenance as arguments,
# calculates a monthly total and an annual total,
# and displays these totals.
def sum_car_expenses(loan, insurance, gas, oil, tires, maintenance):
    # Define local float variables for monthly total and annual total
    monthly_total = float()
    annual_total = float()
    # calculate the monthly total
    monthly_total = loan + insurance + gas + oil + tires + maintenance
    # calculate the annual total
    annual_total = monthly_total * 12

    # Print monthly and annual information, formatting float value to 2 decimal places.
    print("Your monthly total is ", format(monthly_total,'.2f'),
    "\nYour annual total is ", format(annual_total,".2f"))


# Call the main function to start the program
main()
