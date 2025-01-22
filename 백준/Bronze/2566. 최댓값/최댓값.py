n = 9
max_num = -1
max_i, max_j = 0, 0
for i in range(n):
    row = list(map(int, input().split(' ')))
    for j in range(n):
        num = row[j]
        if num > max_num:
            max_num = num
            max_i, max_j = i, j
print(max_num)
print(max_i+1, max_j+1)