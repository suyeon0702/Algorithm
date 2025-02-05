def getGCD(a, b):
    while b != 0:
        a, b = b, a%b
    return a

n = int(input())
r_list = list(map(int, input().split()))
r1 = r_list[0]
for i in range(1, n):
    r = r_list[i]
    gcd = getGCD(r1, r)
    print(f"{r1//gcd}/{r//gcd}")