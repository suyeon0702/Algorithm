num_list = []
for i in range(9):
    n = int(input())
    num_list.append(n)

# max, index로 편하게 가기
# max_num = max(num_list)
# max_num_nth = num_list.index(max_num)+1
# print(max_num)
# print(max_num_nth)

max_num = -1
max_num_nth = 0
for i in range(9):
    num = num_list[i]
    if num > max_num:
        max_num = num
        max_num_nth = i+1
print(max_num)
print(max_num_nth)