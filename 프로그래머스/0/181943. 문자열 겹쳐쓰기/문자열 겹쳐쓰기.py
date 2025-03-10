def solution(my_string, overwrite_string, s):
    head = my_string[:s] + overwrite_string
    tail = my_string[len(head):]
    return head+tail