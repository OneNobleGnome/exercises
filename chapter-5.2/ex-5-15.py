# Programming Exercise 5-15
#
# Program to find the average of five scores and output the scores and average with letter grade equivalents.
# This program prompts a user for five numerical scores,
# calculates their average, and assigns letter grades to each,
# and outputs the list and average as a table on the screen.
from tables import *
# define the main function
def main():
    # define local variables for average and five scores
    average = 0.0
    score_1 = 0.0
    score_2 = 0.0
    score_3 = 0.0
    score_4 = 0.0
    score_5 = 0.0
    # Get five scores from the user
    score_1 = float(input("Enter first score:   "))
    score_2 = float(input("Enter second score:   "))
    score_3 = float(input("Enter third score:   "))
    score_4 = float(input("Enter fourth score:   "))
    score_5 = float(input("Enter fifth score:   "))

    # find the average by passing the scores to a function that returns the average
    average = average_of_5(score_1, score_2, score_3, score_4, score_5)

    # display grade and average information in tabular form
       
    # as score, numeric grade, letter grade, separated by tabs
    print_3_column_header(average, )
    # display a line of underscores under this header
    
    # print data for all five scores, using the score,
    # with the result of a function to determine letter grade

    # display a line of underscores under this table of data

    # display the average and the letter grade for the average



# Define a function to return the average of 5 grades.
# This function accepts five values as parameters,
# computes the average,
# and returns the average.
def average_of_5(num_1, num_2, num_3, num_4, num_5):
    # define a local float variable to hold the average
    average = 0.0
    # calculate the average
    average = (num_1 + num_2 + num_3 + num_4 + num_5)/5
    # return the average
    return(average)


# Define a function to return a numeric grade from a number.
# This function accepts a grade as a parameter,
# Uses logical tests to assign it a letter grade,
# and returns the letter grade.

    # if score is 90 or more, return A
    
    # 80 or more, return B
    
    # 70 or more, return C
    
    # 60 or more, return D
    
    # anything else, return F


# Call the main function to start the program



