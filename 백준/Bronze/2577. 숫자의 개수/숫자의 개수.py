import sys

nums = sys.stdin.read().strip().split('\n')

A, B, C = map(int, nums)

str_result = str(A*B*C)
cnt_list = [0 for _ in range(10)]
for str_num in str_result:
    num = int(str_num)
    cnt_list[num] += 1

for i in range(10):
    print(cnt_list[i])