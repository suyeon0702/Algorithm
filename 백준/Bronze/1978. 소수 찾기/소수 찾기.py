n = int(input())
num_list = list(map(int, input().split(' ')))
prime_cnt = 0
for num in num_list:
    is_prime = True
    if num == 1: 
        continue
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            is_prime = False
            break
    if is_prime:
        prime_cnt += 1
print(prime_cnt)