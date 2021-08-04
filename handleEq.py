ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def evaluateExp(numVar, equation):
    # now to find the number of lines in the actual table using
    # numlines = 2^numVar
    numLines = 2 ** numVar

    #create a dictionary that contains numVar letters of the alphabet, all equal to False
    varDict = {}
    for i in range(numVar):
        varDict[ALPHABET[i]] = False
    print(varDict)
    #break the equation up into a list since strings aren't mutable
    eqList = list(equation)

    #replace all characters that are CAPITAL LETTERS (in ALPHABET) with dict[that letter]
    for i in range(len(eqList)):
        if 65 <= ord(eqList[i]) <= 90:
            eqList[i] = "varDict["+eqList[i]+"]"
    print(eqList)

    #put the string back together
    newEqString = "".join(eqList)
    print(newEqString)

    #

    #my brain is freaking massive