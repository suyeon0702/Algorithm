N = int(input())
last = 0
k = 1
while k*2 <= N:
    k *= 2

if N == k:
    last = k
else:
    last = 2 * (N-k) 

print(last)