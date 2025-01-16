n, b = input().split(' ')
b = int(b)
alp_dict = {}
start_ascii_num = ord("A")
for i in range(26):
    alp_dict[chr(start_ascii_num+i)] = i + 10

sum = 0
for i in range(len(str(n))):
    num = n[i]
    try: num = int(num)
    except: num = alp_dict.get(num)
    sqr_num = len(str(n))-1-i
    sum += b**sqr_num * num

print(sum)