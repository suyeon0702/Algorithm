import sys

n = int(input())
lines = sys.stdin.read().strip().split('\n')
for line in lines:
    a, b = map(int, line.split(' '))
    print(a+b)