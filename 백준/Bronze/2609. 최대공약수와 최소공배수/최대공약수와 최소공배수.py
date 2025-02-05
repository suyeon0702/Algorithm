def getGCD(a, b):
    while b != 0:
        a, b = b, a%b
    return a

a, b = map(int, input().split())
gcd = getGCD(a, b)
lcm = a*b//gcd

print(gcd)
print(lcm)