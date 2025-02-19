import sys
total = int(sys.stdin.readline().strip())
lines = sys.stdin.read().strip().split('\n')
for line in lines:
    total -= int(line)
print(total)