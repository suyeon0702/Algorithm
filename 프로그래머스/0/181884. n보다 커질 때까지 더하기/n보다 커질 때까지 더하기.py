def solution(numbers, n):
    s = 0
    for num in numbers:
        s += num
        if s > n:
            break
    answer = s
    return answer