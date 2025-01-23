def solution(n, control):
    
    for option in control:
        if option == "w": # n이 1 커집니다.
            n += 1
        elif option == "s": # n이 1 작아집니다.
            n -= 1
        elif option == "d": # n이 10 커집니다.
            n += 10
        elif option == "a": # n이 10 작아집니다.
            n -= 10
    answer = n
    return answer

