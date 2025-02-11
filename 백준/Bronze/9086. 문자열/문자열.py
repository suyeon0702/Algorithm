import sys

T = sys.stdin.readline().strip()
lines = sys.stdin.read().strip().split('\n')
for line in lines:
    print(line[0]+line[-1])