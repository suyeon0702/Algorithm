import sys

n = int(input())
lines = sys.stdin.read().strip().split('\n')

stack = []

for line in lines:

    if "push" in line:
        new_num = line.split(' ')[1]
        stack.append(new_num)
    
    elif line == "pop":
        if len(stack) != 0: print(stack.pop())
        else: print(-1)
    
    elif line == "size":
        print(len(stack))

    elif line == "empty":
        if len(stack) == 0: print(1)
        else: print(0)

    elif line == "top":
        if len(stack) == 0: print(-1)
        else: print(stack[-1])
