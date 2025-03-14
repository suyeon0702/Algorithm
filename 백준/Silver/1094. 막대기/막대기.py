X = int(input())

cnt = 0
while X > 0:
    r = X % 2
    X //= 2
    if r: 
        cnt += 1
print(cnt)