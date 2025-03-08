def solution(s):
    q = 0
    if s[0] == "+":
        s = s[1:]
        q = 1
    elif s[0] == "-":
        s = s[1:]
        q = -1
    
    if q == 0:
        answer = int(s)
    else:
        answer = q * int(s)
        
    return answer