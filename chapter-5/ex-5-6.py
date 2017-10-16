# Programming Exercise 5-6
#
# Program to compute calories from fat and carbohydrate.
# This program accepts fat grams and carbohydrate grams consumed from a user,
# uses global constants to calculate the fat calories and carb calories,
# then passes them to a function for formatted display on the screen.


# Global constants for fat calories per gram and carb calories per gram
FAT_CALORIES_PER_G = 20
CARB_CALORIES_PER_G = 10


# define the main function
def main():
    # Define local float variables for grams of fat, grams of carbs, calories from fat,
    # and calories from carbs
    grams_fat = float()
    grams_carbs = float()
    cal_fat = float()
    cal_carb = float()
    # Get grams of fat from the user.
    grams_fat = float(input("Input grams of fat:   "))

    # Get grams of carbs from the user.
    grams_carbs = float(input("Input grams of carbs:   "))

    # Calculate calories from fat.
    cal_fat = grams_fat * FAT_CALORIES_PER_G
    
    # Calculate calories from carbs.
    cal_carb = grams_carbs * CARB_CALORIES_PER_G

    # Call the display calorie detail function, passing grams of fat, grams of carbs,
    # calories from fat and calories from carbs as arguments
    calorie_details(grams_fat,grams_carbs,cal_fat,cal_carb)


# Define a function to display calorie detail.
# This function accepts grams of fat, grams of carbs, calories from fat,
# and calories from carbs as parameters,
# performs no calculations,
# but displays this information formatted for the user.
def calorie_details(grams_fat,grams_carbs,cal_fat,cal_carb):
	# print each piece of information with floats formatted to 2 decimal places.
    print("Grams of fat:   ", format(grams_fat,'.2f'))
    print("Grams of carbs:   ", format(grams_carbs,'.2f'))
    print("Calories from fat:   ", format(cal_fat,'.2f'))
    print("Calories from carbs:   ", format(cal_carb,'.2f'))
# Call the main function to start the program
main()
