def solution(numbers):
    max1 = -1
    max2 = -2
    for num in numbers:
        if max1 < num:
            max2 = max1
            max1 = num
        elif max2 < num:
            max2 = max(max2, num)

    answer = max1 * max2
    return answer