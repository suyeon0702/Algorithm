def solution(num_list):
    answer = 0
    even, odd = [], []
    for num in num_list:
        if num % 2 == 0:
            even.append(str(num))
        else:
            odd.append(str(num))
    even_num = int(''.join(even))
    odd_num = int(''.join(odd))
    answer = even_num + odd_num
    return answer