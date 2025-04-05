def solution(num_list):
    last, front_last = num_list[-1], num_list[-2]
    if last > front_last:
        num_list.append(last-front_last)
    else:
        num_list.append(last*2)
    
    return num_list