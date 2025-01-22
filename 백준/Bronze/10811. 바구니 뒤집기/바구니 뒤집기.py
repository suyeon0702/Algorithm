n, m = map(int, input().split(' '))
bucket_list = [x for x in range(1, n+1)] # 바구니 리스트
for i in range(m):
    i, j = map(int, input().split(' '))
    start_idx, end_idx = i-1, j-1 # 실제 idx로 맞춰주기
    swaped_range = bucket_list[start_idx:end_idx+1][::-1]
    bucket_list[start_idx:end_idx+1] = swaped_range

for i in range(n):
    print(bucket_list[i], end=' ')