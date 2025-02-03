n = int(input())

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

for i in range(n):
    n1, n2 = map(int, input().split())
    print(gcd(n1, n2))
