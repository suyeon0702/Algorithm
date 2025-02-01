n = int(input())
score_list = list(map(int, input().split(' ')))

new_mean = sum(score_list)*100/(max(score_list)*n)
print(new_mean)