string = input()
cnt = 0

for alp in ["a", "e", "i", "o", "u"]:
    cnt += string.count(alp)

print(cnt)