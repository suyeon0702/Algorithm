import sys
N = int(sys.stdin.readline().strip())
n_list = [int(sys.stdin.readline().strip()) for _ in range(N)]
print(sum(n_list))