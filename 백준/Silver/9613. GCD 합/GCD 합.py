def getGCD(a, b):
    while b != 0:
        a, b = b, a%b
    return a

t = int(input())
for i in range(t):
    n_list = list(map(int, input().split()))
    n, n_list = n_list[0], n_list[1:]
    gcd_sum = 0
    for j in range(n-1):
        for k in range(j+1, n):
            a, b = n_list[j], n_list[k]
            gcd = getGCD(a, b)
            gcd_sum += gcd
    print(gcd_sum)