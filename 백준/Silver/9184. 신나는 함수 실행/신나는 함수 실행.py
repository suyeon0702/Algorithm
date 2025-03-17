import sys

dp = [[[-1]*21 for _ in range(21)] for _ in range(21)]
def exciting_func(a, b, c):
    
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return exciting_func(20, 20, 20)
    else:
        if dp[a][b][c] != -1:
            return dp[a][b][c]
        elif a < b < c:
            dp[a][b][c] = exciting_func(a, b, c-1) + exciting_func(a, b-1, c-1) - exciting_func(a, b-1, c)
            return dp[a][b][c]
        else:
            dp[a][b][c] = exciting_func(a-1, b, c) + exciting_func(a-1, b-1, c) + exciting_func(a-1, b, c-1) - exciting_func(a-1, b-1, c-1)
            return dp[a][b][c]

# w1, w2, w3 = map(int, input().split())
lines = sys.stdin.read().strip().split('\n')
for line in lines:
    w1, w2, w3 = map(int, line.strip().split())
    if (w1, w2, w3) == (-1, -1, -1):
        break
    result = exciting_func(w1, w2, w3)
    print(f"w({w1}, {w2}, {w3}) = {result}")