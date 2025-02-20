import sys
n, h, v = map(int, sys.stdin.readline().strip().split())
print(4*max(h, n-h)*max(v, n-v))