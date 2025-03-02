def solution(arr, flag):
    answer = []
    for num, f in zip(arr, flag):
        if f:
            answer.extend([num]*num*2)
        else:
            for i in range(num):
                answer.pop()
    return answer