def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    lcm = int(a*b/gcd(a,b))
    print(lcm)