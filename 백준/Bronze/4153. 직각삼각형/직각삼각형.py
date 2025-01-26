import sys

lines = sys.stdin.read().strip().split('\n')
for line in lines:
    len_list = list(map(int, line.split(' ')))
    if sum(len_list) == 0:
        break
    len_list.sort()
    if len_list[0]**2 + len_list[1]**2 == len_list[2]**2:
        print("right")
    else:
        print("wrong")
