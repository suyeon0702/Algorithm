import sys

n = int(input())
int_stack = []
lines = sys.stdin.read().strip().split('\n')
for line in lines:
    order_list = list(map(int, line.split()))
    order = order_list[0]
    if order == 1: # insert
        new_num = order_list[1]
        int_stack.append(new_num)
    elif order == 2: # pop
        if len(int_stack) == 0: print(-1)
        else: print(int_stack.pop())
    elif order == 3: # len
        print(len(int_stack))
    elif order == 4: # isEmpty
        if len(int_stack) == 0: print(1)
        else: print(0)
    elif order == 5: # peek
        if len(int_stack) == 0: print(-1)
        else: print(int_stack[-1])