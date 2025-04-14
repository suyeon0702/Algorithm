import sys
lines = sys.stdin.read().strip().split('\n')
weights = list(map(int, lines))
weights = sorted(weights)
print(weights[1])