n = int(input())
num_list = list(map(int, input().split(' ')))

if n == 1:
    max_num = min_num = num_list[0]
else:
    # min, max 안 쓰고 해보기
    if num_list[0] > num_list[1]:
        max_num, min_num = num_list[0], num_list[1]
    else:
        max_num, min_num = num_list[1], num_list[0]
    for i in range(2, n):
        num = num_list[i]
        if num > max_num:
            max_num = num
        else:
            if num < min_num:
                min_num = num

print(f"{min_num} {max_num}")