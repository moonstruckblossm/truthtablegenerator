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

    #slice the alphabet upto the last letter we're using and reverse it
    alphSlice = ALPHABET[0:numVar]
    alphSlice = alphSlice[::-1]

    #break the equation up into a list since strings aren't mutable
    eqList = list(equation)

    #replace all characters that are CAPITAL LETTERS (in ALPHABET) with dict[that letter]
    for i in range(len(eqList)):
        if 65 <= ord(eqList[i]) <= 90:
            eqList[i] = "varDict['"+eqList[i]+"']"
    print(eqList)

    dictList = []

    #put the string back together
    newEqString = "".join(eqList)
    print(newEqString)


    #ACTUALLY PRINTING THE THING LOL
    print("\033[1;95;40m♡♡ YOUR TRUTH TABLE ♡♡\033[0m")

    print()

    #header string
    header = "\033[4;95;40m"
    for i in alphSlice[::-1]:
        header += i+"  "
    header += "Result\033[0m"

    print(header)

    #for each number in the number of lines
    for i in range(numLines):
        #check each num in the num of variables to see if it's time to alternate?
        for j in range(len(alphSlice)):
            if i%(2**j) == 0:
                dictPiece = {alphSlice[j] : not varDict[alphSlice[j]]}
                varDict.update(dictPiece)
        print(eval(newEqString))





    #my brain is freaking massive