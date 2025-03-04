def solution(my_string, queries):
    my_list = list(my_string)
    for q in queries:
        start, end = q[0], q[1]
        target_range = my_list[start:end+1]
        for i in range(len(target_range)):
            alp = target_range.pop()
            my_list[start+i] = alp
    answer = ''.join(my_list)
    return answer