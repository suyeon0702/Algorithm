num, k = map(int, input().split(' '))
is_prime = [True] * (num+1)
is_prime[0] = is_prime[1] = False

cnt = 0 # 제거 카운트
k_num = 0 # k번째 제거된 수
for i in range(2, num+1):
    if is_prime[i]:
        # p 제거
        is_prime[i] = False
        cnt += 1
        if cnt == k:
            k_num = i
            break
        # p 배수 제거
        for j in range(i*i, num+1, i):
            if is_prime[j]: # 이미 제거된 것은 pass
                is_prime[j] = False
                cnt += 1
                if cnt == k:
                    k_num = j
                    break
print(k_num)