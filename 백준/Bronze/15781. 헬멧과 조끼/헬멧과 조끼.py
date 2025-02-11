import sys

N, M = map(int, sys.stdin.readline().strip().split())
n_list = list(map(int, sys.stdin.readline().strip().split()))
m_list = list(map(int, sys.stdin.readline().strip().split()))
print(max(n_list)+max(m_list))