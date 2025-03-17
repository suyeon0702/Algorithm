def fibo_dp(n):
    dp = [0] * (n+1)
    dp[1] = dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

n = int(input())
fibo_rec_cnt = fibo_dp(n)
fibo_dp_cnt = n-2
print(fibo_rec_cnt, fibo_dp_cnt)