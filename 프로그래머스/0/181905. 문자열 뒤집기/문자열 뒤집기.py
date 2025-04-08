def solution(my_string, s, e):
    mid = my_string[s:e+1]
    reverse_mid = mid[::-1]
    return my_string[:s] + reverse_mid + my_string[e+1:]