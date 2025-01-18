num_list = []
for i in range(9):
    n = int(input())
    num_list.append(n)
max_num = max(num_list)
max_num_nth = num_list.index(max_num)+1
print(max_num)
print(max_num_nth)