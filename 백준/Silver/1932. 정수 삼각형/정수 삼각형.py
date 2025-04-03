import sys
lines = sys.stdin.read().strip().split('\n')

n = int(lines[0])
triangle = []
for i in range(n):
    triangle.append(list(map(int, lines[i+1].strip().split())))

dp_sum = [[0]*(i+1) for i in range(n)]
dp_sum[0][0] = triangle[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0: # 왼쪽 끝
            dp_sum[i][j] = dp_sum[i-1][j] + triangle[i][j]
        elif j == i: # 오른쪽 끝
            dp_sum[i][j] = dp_sum[i-1][j-1] + triangle[i][j]
        else: # 왼쪽 위, 오른쪽 위 비교
            dp_sum[i][j] = max(dp_sum[i-1][j-1], dp_sum[i-1][j]) + triangle[i][j]

print(max(dp_sum[-1]))