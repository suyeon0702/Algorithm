white_paper = [[0 for _ in range(100)] for _ in range(100)]
paper_num = int(input())
side_len = 10
for paper in range(paper_num):
    x, y = map(int, input().split(' '))
    for i in range(x, x+10): # 도화지 채우기
        for j in range(y, y+10):
            white_paper[i][j] = 1
# 총 넓이 계산
total_area = sum([sum(row) for row in white_paper])
print(total_area)