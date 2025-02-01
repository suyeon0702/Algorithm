import sys

lines = sys.stdin.read().strip().split('\n')
for line in lines:
    a, b = map(int, line.split(' '))
    if a+b == 0: break
    print(a+b)