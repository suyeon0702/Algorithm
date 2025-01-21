tasecase = int(input())
for i in range(tasecase):
    num_list = list(map(int, input().split(' ')))
    min_even = 100
    even_sum = 0
    for num in num_list:
        is_even = (num%2 == 0)
        if is_even:
            if num < min_even: # 최소 짝수 갱신
                min_even = num
            even_sum += num # 짝수 합 갱신
    print(even_sum, min_even)