'''Hi hello wow ok
um hi my name's kai and um
this is my truth table generator! at least, a very early version of it!
currently, since this is for a project that needed to be put together within about three days,
there isn't too much functionality! but i promise it's the cutest truth table generator you'll ever see!
'''

from handleEq import *
from utilityFunctions import *

def main():
    #intro and information
    print("\033[1;95;40m♡ Welcome to MARU'S TRUTH TABLE GENERATOR! ♡\033[0m")
    print()
    print("\033[4;96;40m♡ KEY ♡\033[0m\n"
          " \n"
          "♡ '&' or 'and' = LOGICAL AND\n"
          "♡ '|' or 'or' = LOGICAL OR\n"
          "♡ '!' or 'not' = LOGICAL NOT/INVERT\n"
          "♡ '^' = LOGICAL XOR\n"
          "♡ you can put a ! in front of an 'and', 'or', or '^' (xor) expression to make a NAND, NOR "
          "or XNOR function!")
    print()
    print("\033[4;96;40m♡ EXAMPLES ♡\033[0m\n")
    print("♡ !(A and B) | (B ^ C) || This is how you would enter (A NAND B) OR (B XOR C)")
    #so you CAN pass in functions for your uhhhh eval

    print()

    #actually getting the equation lmao?

    print("\033[1;93;40mlet's get started! ☆\033[0m\n")

    #for now we can assume that the number of vars the user snters is accurate to the yknow ACTUAL NUMBER
    equation = input("♡ Input a logical equation using capital variables such as A, B, C, D, etc: ")

    #finds the amount of variables in the equation.
    #for now we can assume that, if a letter is entered, the user has entered all of the letters preceding it
    numVar = findGreatest(equation)
    print(numVar, "variables detected!")

    #finally, we can actually pass in the number of lines and the equation!
    evaluateExp(numVar, equation)

main()