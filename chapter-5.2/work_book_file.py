#prompt
#choose
#display

import circle
import rectangle



AREA_OF_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5



choice = 0

def handle_area_of_circle():
    radius = float(input("Enter the circle's radius: "))
    return"The area is" + str(circle.area_radius(radius))
def handle_circumference_of_circle():
    radius = float(input("Enter the circles radius: "))
    return "The circumference is" + str(circle.circumference(radius))
def handle_area_of_rectangle():
    width = float(input("Enter the rectangle's width: "))
    length = float(input("Enter the rectangle's length: "))
def handle_perimeter_of_rectangle():
    width = float(input("Enter the rectangle's width: "))
    length = float(input("Enter the rectangle's length: "))
    
def handle_choices(choice):
    if choice == AREA_OF_CIRCLE_CHOICE:
        return handle_area_of_circle()
    elif choice == CIRCUMFERENCE_CHOICE:
        return handle_circumference_of_circle()
    elif choice == AREA_RECTANGLE_CHOICE:
        return handle_area_of_rectangle()
    elif choice == PERIMETER_RECTANGLE_CHOICE:
        return handle_perimeter_of_rectangle()
    elif choice == QUIT_CHOICE:
        return "Exiting the program..."
    else:
        return "Error: Invalid selection."



def display_menu():
    print(" MENU")
    print("1) Area of a circle")
    print("2) Circumference of a circle")
    print("3) Area of a rectangle")
    print("4) Perimeter of a rectangle")
    print("5) Quit")



def area_and_perimeter_function():
    choice = 0
    while choice != QUIT_CHOICE:
        display_menu()
        
        choice = int(input("Enter your choice: "))

        output = handle_choices(choice)
        
        print(output)



def ask_for_choice():
    global choice
    choice = int(input("Enter your choice: "))



def main():
    global choice
    
    choice = 0
    while choice != QUIT_CHOICE:
        
        global choice
        display_menu()
        
        ask_for_choice()

        output = handle_choices(choice)
        
        print(output)





    
if __name__ == main():
    main()
