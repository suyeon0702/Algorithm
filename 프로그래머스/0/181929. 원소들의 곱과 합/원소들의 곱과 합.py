def solution(num_list):
    a = 1
    b = 0
    
    for num in num_list:
        a *= num
        b += num
    b = b**2
    
    return int(a < b)