def solution(numbers):
    str_numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(10):
        numbers = numbers.replace(str_numbers[i], str(i))
    answer = int(numbers)
    return answer