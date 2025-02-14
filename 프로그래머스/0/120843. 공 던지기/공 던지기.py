def solution(numbers, k):
    idx = (2*(k-1))%len(numbers)
    answer = numbers[idx]
    return answer