import sys

descending_stack = []
n = int(input())
bar_list = [int(sys.stdin.readline().strip()) for _ in range(n)]
for bar_h in bar_list:

    if len(descending_stack) == 0:
        descending_stack.append(bar_h)
    else:
        while len(descending_stack) > 0 and descending_stack[-1] <= bar_h:
            descending_stack.pop()
        descending_stack.append(bar_h)

print(len(descending_stack))