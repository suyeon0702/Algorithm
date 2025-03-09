N, K = map(int, input().split())

table = list(range(1, N+1))
josephus = []

idx = K-1
while 1:
    if len(table) == 0:
        break
    
    idx %= len(table)
    josephus.append(str(table.pop(idx)))
    idx = idx + K - 1

print(f"<{', '.join(josephus)}>")