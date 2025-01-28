# 에라토스테네스의 체 활용
def sieve_of_eratosthenes(start, end):
    # 모든 수를 소수라 가정
    is_prime = [True] * (end+1)
    # 0과 1은 소수가 아니므로 False 처리
    is_prime[0] = is_prime[1] = False

    # 2부터 end의 제곱근까지만 검사 -> 제곱근 이후의 수는 이미 이전 수의 배수로 처리됨
    # ex) end가 100이라면 2~10까지만 확인하면 됨. 11~ 부터는 이전 수의 배수로 처리되거나 배수가 100을 초과함
    for i in range(2, int(end**0.5)+1):
        if is_prime[i]: # == True
            # i의 배수 False 처리 (i씩 점프하며 세면서 배수 확인)
            for j in range(i*i, end+1, i): # 제곱부터 시작해도 무방 (ex. 5x2, 5x3, 5x4는 이전 단계에서 이미 제거됨)
                is_prime[j] = False
    
    # 소수만 리스트에 추가하여 반환
    result = [i for i in range(start, end+1) if is_prime[i]]
    return result


start, end = map(int, input().split(' '))
result_list = sieve_of_eratosthenes(start, end)
for i in result_list:
    print(i)