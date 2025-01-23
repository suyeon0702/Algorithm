import sys

n = int(input())
lines = sys.stdin.read().strip().split('\n')

str_len_list = [[] for _ in range(51)]
for line in lines:
    word = line
    str_len = len(line)
    str_len_list[str_len].append(word)

for word_list in str_len_list:
    if len(word_list) == 0:
        pass
    else:
        word_list = list(set(word_list)) # 중복값 제거
        word_list.sort()
        for word in word_list:
            print(word)