while 1:
    n = input()
    if n == "0":
        break
    
    list_n = list(n)
    reverse_n = ''
    for i in range(len(list_n)):
        reverse_n += list_n.pop()

    if n == reverse_n: print("yes")
    else: print("no")