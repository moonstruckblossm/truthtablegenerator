'''Hi hello wow ok
um hi my name's kai and um
this is my truth table generator! at least, a very early version of it!
currently, since this is for a project that needed to be put together within about three days,
there isn't too much functionality!
'''

from handleEq import *

def main():
    #intro and information
    print("Welcome to MARU'S TRUTH TABLE GENERATOR!")
    print()
    print("KEY\n"
          "-'&'/'and' = LOGICAL AND\n"
          "-'|'/'or' = LOGICAL OR\n"
          "-'!'/'not = LOGICAL NOT/INVERT\n"
          "-'^' = LOGICAL XOR\n"
          "-you can put a ! in front of an 'and', 'or', or '^' (xor) expression to make a NAND, NOR "
          "or XNOR function!")
    print()
    print("EXAMPLES")
    print("!(A and B) | (B ^ C) || This is how you would enter (A NAND B) OR (B XOR C)")
    #so you CAN pass in functions for your uhhhh eval

    print()

    #actually getting the equation lmao?
    equation = input("Input a logical equation using the variables A, B, C, and D!")
