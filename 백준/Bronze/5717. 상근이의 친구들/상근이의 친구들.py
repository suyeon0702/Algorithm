import sys

lines = sys.stdin.read().strip().split('\n')

for line in lines:
    m, f = map(int, line.strip().split())
    if m == 0 and f == 0:
        break
    print(m+f)