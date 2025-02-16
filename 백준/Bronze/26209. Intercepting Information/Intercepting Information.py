import sys
bits = list(map(int, sys.stdin.readline().strip().split()))
is_success = "S"
for bit in bits:
    if bit == 9:
        is_success = "F"
        break
print(is_success)