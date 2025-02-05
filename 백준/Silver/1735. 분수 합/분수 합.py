# A/B + C/D = X/Y = num*gcd(x, y) / denum*gcd(x, y)
def getGCD(a, b):
    while b != 0:
        a, b = b, a%b
    return a

a, b = map(int, input().split())
c, d = map(int, input().split())

x = a*d + b*c
y = b*d

gcd = getGCD(x, y)
num, denum = x//gcd, y//gcd
print(f"{num} {denum}")