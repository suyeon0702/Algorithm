descending_stack = []
n = int(input())
for i in range(n):
    bar_h = int(input())

    if len(descending_stack) == 0:
        descending_stack.append(bar_h)
    else:
        while len(descending_stack) > 0 and descending_stack[-1] <= bar_h:
            descending_stack.pop()
        descending_stack.append(bar_h)

print(len(descending_stack))