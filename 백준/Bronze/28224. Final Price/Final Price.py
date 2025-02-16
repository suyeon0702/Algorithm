import sys
N = int(sys.stdin.readline().strip())
price_change_amount = list(map(int, sys.stdin.read().strip().split('\n')))
print(sum(price_change_amount))