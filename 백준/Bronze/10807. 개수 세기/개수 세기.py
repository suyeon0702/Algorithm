import sys
lines = sys.stdin.read().strip().split('\n')
N = int(lines[0])
num_list = list(map(int, lines[1].split()))
target_num = int(lines[2])

print(num_list.count(target_num))