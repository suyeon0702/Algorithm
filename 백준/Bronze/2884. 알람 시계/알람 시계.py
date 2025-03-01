import sys
H, M = map(int, sys.stdin.readline().strip().split())

if M >= 45:
    M -= 45
else:
    H -= 1
    M += 15
    H = (H+24)%24

print(f"{H} {M}")