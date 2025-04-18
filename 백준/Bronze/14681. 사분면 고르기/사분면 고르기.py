x = int(input())
y = int(input())

x_plus = (x > 0)
y_plus = (y > 0)

if y_plus:
    if x_plus: print(1)
    else: print(2)
else:
    if x_plus: print(4)
    else: print(3)