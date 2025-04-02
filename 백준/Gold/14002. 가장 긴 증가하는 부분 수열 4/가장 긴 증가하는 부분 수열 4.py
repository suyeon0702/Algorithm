N = int(input())
A = list(map(int, input().split()))

dp = [1] * N
prev = [-1] * N

for i in range(N):
    for j in range(i):
        if A[j] < A[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            prev[i] = j

max_length = max(dp)
last_idx = dp.index(max_length)

print(max_length)

# 역추적
lis = []
while last_idx != -1:
    lis.append(A[last_idx])
    last_idx = prev[last_idx]

# LIS 수열 출력
print(*lis[::-1])