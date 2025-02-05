def solution(lines):
    indexed_line = [0 for _ in range(202)]
    for line in lines:
        for i in range(line[0], line[1]):
            indexed_line[i+100] += 1
    answer = len([num for num in indexed_line if num >= 2])
    
    return answer