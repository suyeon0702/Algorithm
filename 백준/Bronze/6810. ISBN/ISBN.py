import sys
lines = sys.stdin.read().strip().split('\n')

end = ''.join(lines)
front = "9780921418"
isbn = front+end
s = 0
for i in range(1, len(isbn), 2):
    s += int(isbn[i])
s *= 3
for i in range(0, len(isbn), 2):
    s += int(isbn[i])

print(f"The 1-3-sum is {s}")