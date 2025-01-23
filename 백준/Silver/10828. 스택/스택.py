stack = []
n = int(input())

for i in range(n):
    user_input = input()
    if "push" in user_input:
        new_num = user_input.split(' ')[1]
        stack.append(new_num)
    
    elif user_input == "pop":
        if len(stack) != 0: print(stack.pop())
        else: print(-1)
    
    elif user_input == "size":
        print(len(stack))

    elif user_input == "empty":
        if len(stack) == 0: print(1)
        else: print(0)

    elif user_input == "top":
        if len(stack) == 0: print(-1)
        else: print(stack[-1])