import sys
lines = sys.stdin.read().strip().split('\n')
N = int(lines[0])
T = int(lines[1])
apart = list(map(int, lines[2].split()))
b_list = list(map(int, lines[3].split()))

bottom_idx = 0
fail_list = []
for b in b_list:
    bottom_idx = (bottom_idx + b-1) % (2*N)
    fail_list.append(str(apart[bottom_idx]))

print(" ".join(fail_list))