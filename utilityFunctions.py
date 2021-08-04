ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#this will return the amount of arguments in the equation based on what the user's greatest capital letter is

def findGreatest(string):
    flag = True
    index = 0
    while flag:
        #if the given letter is in the string
        if ALPHABET[index] in string:
            index += 1
            pass
        else:
            print("STOP! highest letter is ", ALPHABET[index-1])
            flag = False
    return index