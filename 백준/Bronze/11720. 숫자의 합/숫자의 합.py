n = int(input())
n_str = input()
s = 0
for i in range(len(n_str)):
    num = int(n_str[i])
    s += num

print(s)