N = int(input())

cards = list(range(1, N+1))

front = 0
rear = N-1

last = 0
while front != rear:
    # first
    front += 1
    # second
    cards.append(cards[front])
    front += 1
    rear += 1

last = cards[front]
print(last)