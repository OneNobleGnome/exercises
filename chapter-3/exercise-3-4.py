# Programming Exercise 3-4
#
# Program to convert a number from 1 to 10 to a Roman numeral.
# This program will accept an integer from 1 to 10 from the user
# and use it to choose an appropriate Roman numeral
# to display on the screen.

# Variables to hold a number and a numeral.
# initialize the number as an int and the numeral as a string.
number = int()
numeral = str("numeral")
# Get number from user and convert it to an int
number = int(input("Enter a number(1-10)"))

I = 1
V = 5
X = 10

# Set numeral to a Roman numeral value based on the value of number
# use a set of if ... elif .... etc. statements.
if  number == 1:
    numeral = "I"
elif number == 2:
    numeral = "II"
elif number == 3:
    numeral = "III"
elif number == 4:
    numeral = "IV"
elif number == 5:
    numeral = "V"
elif  number == 6:
    numeral = "VI"
elif number == 7:
    numeral = "VII"
elif number == 8:
    numeral = "VIII"
elif number == 9:
    numeral = "IX"
elif number == 10:
    numeral = "X"
else:
    print("value isn't in 0-10")






# use a final else to display an error if number is out of range.


# display the numeral on the screen.
print("Your number was:",number,"\nIt is equal to",numeral)



numList = [] 
maxLengthList = 6
while len(numList) < maxLengthList:
    item = input("Enter your Item to the List: ")
    numList.append(item)
    print (numList)
print ("That's your number List")
print (numList)

