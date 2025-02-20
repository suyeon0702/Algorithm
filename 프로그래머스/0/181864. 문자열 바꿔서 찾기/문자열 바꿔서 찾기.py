def solution(myString, pat):
    new_pat = ""
    for p in pat:
        if p == "A": 
            new_pat += "B"
        elif p == "B":
            new_pat += "A"
    return int(new_pat in myString)