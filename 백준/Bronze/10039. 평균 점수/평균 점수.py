import sys

score_list = [max(int(sys.stdin.readline().strip()), 40) for _ in range(5)]
print(sum(score_list)//5)