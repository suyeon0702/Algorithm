a, b, = map(int, input().split())

start_idx = end_idx = 0
i = 0
total = 0
while 1:
    start_idx += i
    i+=1
    end_idx = start_idx + i

    if start_idx > 1000:
        break
    if a > b:
        break
    
    if a > start_idx and a <= end_idx:
        total += i*(min(b, end_idx)-a+1)
        a = end_idx+1

print(total)