import sys
T = int(sys.stdin.readline().strip())
for i in range(T):
    V, E = map(int, sys.stdin.readline().strip().split())
    print(2-V+E)