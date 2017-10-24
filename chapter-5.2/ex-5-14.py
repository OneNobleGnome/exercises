# Programming Exercise 5-14
#
# Program to compute kinetic energy from mass and velocity.
# This program accepts values for mass and velocity from the user in kilograms and meters per second,
# passes them to a function that returns kinetic energy in joules calculated from those values,
# and displays the result.


# define the main function
def main():
    # define local float variables for mass, velocity and kinetic energy
    mass = float()
    velocity = float()
    kinetic = float()

    # Get mass from user
    mass = float(input("enter the mass:   "))

    # Get velocity from user
    velocity = float(input("enter the velocity:   "))

    # Get kinetic energy in joules from the kinetic energy function
    # Display kinetic energy in joules, formatted to 2 decimal places.
    print(format(find_kinetic_energy(mass, velocity),'.2f'))


# Define a function to calculate kinetic energy in joules.
# The function accepts two parameters, mass in kilograms and velocity in meters/second,
# uses a formula to calculate the joules of kinetic energy,
# and returns the result
def find_kinetic_energy(mass, velocity):
    # Define a local variable for joules of kinetic energy
    kinetic_energy = float()
	# calculate the kinetic energy using the parameters and the conversion formula    
    kinetic_energy = mass * velocity
	# return the result
    return(kinetic_energy)


# Call the main function to start the program
main()


