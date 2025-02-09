output_list = [-1 for _ in range(26)]

s = input()
a_ordnum = ord('a')
for i in range(len(s)):
    alp = s[i]
    idx = ord(alp) - a_ordnum
    if output_list[idx] != -1:
        pass
    else:
        output_list[idx] = i

for num in output_list:
    print(num, end=' ')