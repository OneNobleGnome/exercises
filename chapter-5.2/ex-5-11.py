# Programming Exercise 5-11
#
# Program to quiz a user with a random addition problem.
# This program uses a random function to generate addends for an addition problem,
#   calls a function to display the problem, passing the operands as arguments,
#   calls a second function to prompt the user for an answer to the problem,
# it calculates the correct answer,
# then passes the user answer and correct answer to a third function to evaluate the results,
#   and display whether the user was correct or not.



# to generate random numbers, import random module
import random


# define the main function
def main():
	
    MIN = 0
    MAX = 10

    
    addend_1 = int()
    addend_2 = int()
    addend_3 = int()
    
    
    addend_1, addend_2 = generate_random_ints(MIN,MAX)
    correct_answer = calculate_correct_answer(addend_1, addend_2)
    
    
    display_addition_problem(addend_1, addend_2)
    user_answer = prompt_for_answer()
    evaluate_answer(correct_answer, user_answer)


# this isn't being used right now
def generate_random_int(min_value, max_value):
    return 5
    
    
    
def generate_random_ints(min_value, max_value):
    x = random.randint(min_value, max_value)
    y = random.randint(min_value, max_value)
    return x, y
def calculate_correct_answer(a, b):
    return(a + b)
def display_addition_problem(a, b):
    line_1 = format(a,'5')
    line_2 = "+" + format(b, '4')
    
    print(line_1)
    print(line_2)
    
def prompt_for_answer():
    user_entry = int(input("Enter answer:   "))
    return(user_entry)
    
def evaluate_answer(correct_answer, user_answer):
    print("correct_answer is ", correct_answer, correct_answer.__class__)
    print("user_answer is ", user_answer )
    if user_answer == correct_answer:
        print("You did it")
    else:
        print("Wrong answer")

main()