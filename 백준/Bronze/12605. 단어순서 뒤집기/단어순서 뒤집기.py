n = int(input())
for i in range(n):
    str_list = input().split()
    print(f"Case #{i+1}: ", end='')
    while 1:
        try:
            print(str_list.pop(), end=' ')
        except:
            print()
            break