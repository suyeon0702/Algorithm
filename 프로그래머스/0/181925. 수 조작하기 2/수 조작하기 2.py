def solution(numLog):
    answer = ''
    for i in range(len(numLog)-1):
        before = numLog[i]
        after = numLog[i+1]
        r = after-before
        if r == 1: con = 'w'
        elif r == -1: con = 's'
        elif r == 10: con = 'd'
        elif r == -10: con = 'a'
        answer += con
    
    return answer