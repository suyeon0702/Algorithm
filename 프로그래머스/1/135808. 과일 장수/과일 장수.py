def solution(k, m, score):
    score.sort(reverse=True)
    answer = 0
    for i in range(0, len(score), m):
        one_box = score[i:i+m]
        if len(one_box) < m:
            continue
        min_apple = one_box[-1]
        box_score = min_apple * m
        answer += box_score
    
    return answer