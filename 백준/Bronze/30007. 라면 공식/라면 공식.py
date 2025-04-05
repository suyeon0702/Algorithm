import sys
lines = sys.stdin.read().strip().split('\n')
n = int(lines[0])
for i in range(1, n+1):
    a, b, x = map(int, lines[i].strip().split())
    w = a*(x-1)+b
    print(w)