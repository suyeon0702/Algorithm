black_board = []
result_string = ''
max_col_cnt = 0
for i in range(5): # 글자 붙이기
    row = list(input())
    black_board.append(row)
    if len(row) > max_col_cnt:
        max_col_cnt = len(row)
for j in range(max_col_cnt): # 글자 읽기
    for i in range(5):
        try: code = black_board[i][j]
        except: code = ''
        result_string += code
print(result_string)