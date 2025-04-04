import sys
lines = sys.stdin.read().strip().split('\n')
money = 0
for line in lines:
    if line == "-1":
        break
    money += int(line)
print(money)