import sys
N, M = map(int, sys.stdin.readline().strip().split())
is_enough = 100*N >= M

if is_enough: print("Yes")
else: print("No")