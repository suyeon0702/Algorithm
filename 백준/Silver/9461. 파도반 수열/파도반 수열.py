import sys

T = int(input())
lines = sys.stdin.read().strip().split()

for line in lines:
    N = int(line)
    k_list = [1, 1, 1, 2, 2]
    # a + b = c
    a_idx = 4
    b_idx = 0

    cycle = N-len(k_list) # = N-5

    for i in range(cycle):
        c = k_list[a_idx] + k_list[b_idx]
        k_list.append(c)
        a_idx += 1
        b_idx += 1

    print(k_list[N-1])