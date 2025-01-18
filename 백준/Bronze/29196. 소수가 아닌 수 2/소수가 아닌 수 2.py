num = input()
str_p = num.split('.')[1]
p = int(str_p)
q = 10**(len(str_p))
print("YES")
print(p, q)