def parseStringToArray(string):
    word = ""
    string = string
    returnArray = []
    for character in string:
        if character == " ":
            returnArray.append(word)
            word = ""
        else:
            word += character
    if word:
        returnArray.append(word)
    return returnArray

def parseArrayToString(array):
    return " ".join(array)
