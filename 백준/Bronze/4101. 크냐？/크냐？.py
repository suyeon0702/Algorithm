import sys

lines = sys.stdin.read().strip().split('\n')

for line in lines:
    a, b = map(int, line.strip().split())
    if a == 0 and b == 0:
        break
    print("Yes") if a > b else print("No")