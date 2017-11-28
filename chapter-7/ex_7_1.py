# Programming Exercise 7-1
#
# Program to Total a week's sales (seven inputs).
# This program prompts a user for a sales amount for each day of the week,
# totals them up, then displays the total formatted as currency.
rtotal_sales = 0.0

def test_input(subject):
    try:
        float(subject)
        return(True)
    except TypeError: 
        print("your value was unacceptable")
    except ValueError:
        print("got: value error\nEnter a different number")



def main():
# Define the main function
    rtotal_sales = 0.0
    # Define local float variable for rtotal sales
    daily_sales = [0,0,0,0,0,0,0]
    days_o_week = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    # Initialize lists for daily sales and days of the week (7 elements each)
    for i in range(7):
    # loop 7 times
        value = False
        while not value:
            daily_sales[i] = input("day of the week, ", str.format(days_o_week[i])         #errors when your enter a string in here
            # get the daily sales for the current day by name
            # use a function to validate the input can be cast to a float
            value = test_input(daily_sales[i])
        # add the daily sales to the total
        rtotal_sales += float(daily_sales[i])

    # Display total sales; use a $ and format the value to two decimal places
    print("$",format(rtotal_sales,'.2f'))

# Include a function to ensure the program has valid float values
    if rtotal_sales != format(rtotal_sales,'.2'):
        print("your program did not error")
    else:
        print("your program errored")

# Call the main function to start the program
main()
