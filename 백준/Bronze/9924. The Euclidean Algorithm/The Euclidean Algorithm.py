a, b = map(int, input().split())
cnt = 0
while a != b:
    a, b = max(a,b)-min(a,b), min(a,b)
    cnt += 1
print(cnt)