def solution(array):
    max_num = -1
    max_idx = -1
    for i in range(len(array)):
        if array[i] > max_num:
            max_num = array[i]
            max_idx = i
    answer = [max_num, max_idx]
    return answer