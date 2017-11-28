# Programming Exercise 7-3
#
# Program to compute simple statistics for one year of monthly rainfall.
# This program prompts the user for 12 monthly rainfall values,
# calculates the total and average, finds the high and low values,
# and displays the results on the screen.


def test_input(subject):
    try:
        float(subject)
        return(True)
    except TypeError: 
        print("your value was unacceptable")
    except ValueError:
        print("got: value error\nEnter a different number")


# define the main function
def main():
    
    # define local float variables for total, average, high and low rainfall
    total = 0.0
    average = 0.0
    high = 0.0
    low = 0.0
    
    # define local string values for high month, low month and rainfall input
    high_month = ""
    low_month = ""
    rainfall_input = ""

    # define a list of floats to hold 12 monthly rainfall amounts
    rain_per_month = [0,0,0,0,0,0,0,0,0,0,0,0]
    
    # define a list for month names initialized with names for all 12 months.
    months = ["January", "Feburary", "March", "April", "May", "June", "July", "August", "September","October","November", "December"]

    # loop through the monthly rainfall list
    for i in range(len(rain_per_month)):
        
        
        value = False
        while not value:
            # prompt the user for rainfall input, using the month name in the prompt
            rainfall_input = input("Then amount of rainfall for, " + months[i])
            # use a function to make sure rainfall input can be cast to a float
            value = test_input(rainfall_input)
            
        # assign rainfall input value to the current item in monthly rainfall list
        rainfall_input = float(rainfall_input)
        rain_per_month[i] = rainfall_input

    # Calculate the total of monthly rainfall
    total = sum(rain_per_month)
    # Calculate the average monthly rainfall
    average = (sum(rain_per_month))/12
    # find the high (max) rainfall
    high = max(rain_per_month)
    # use the index of the high rainfall to find the month name for high rainfall
    high_month = months[rain_per_month.index(high)]
    # find the low (min) rainfall
    low = min(rain_per_month)
    # use the index of the low rainfall to find the month name for low rainfall
    low_month = months[rain_per_month.index(low)]
    # Display results appropriately, formatting float values to two decimal places
    print("total:   ",format(total,'.2f'))
    print("average:   ",format(average,'.2f'))
    print("high:  ",format(high,'.2f'),",",high_month)
    print("low:  ",format(low,'.2f'),",",low_month)
    


# function to validate float input
    if total == format(total,'.2f') and average == format(average,'.2f'):
        print("your program did not error")
        
    else:
        print("your program errored")
    

# Call the main function.


main()