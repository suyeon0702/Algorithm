def solution(myString):
    newString = ""
    for alp in myString:
        if alp < 'l': newString += 'l'
        else: newString += alp
    return newString