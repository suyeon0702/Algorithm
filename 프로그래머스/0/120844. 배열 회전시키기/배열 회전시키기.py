def solution(numbers, direction):
    if direction == "left":
        answer = numbers[1:] + numbers[0:1]
    elif direction == "right":
        answer = numbers[-1:] + numbers[:len(numbers)-1]
    return answer