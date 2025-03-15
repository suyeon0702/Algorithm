def solution(dots):
    x = list(set([dot[0] for dot in dots]))
    y = list(set([dot[1] for dot in dots]))
    w, h = x[0] - x[1], y[0] - y[1]
    answer = w*h
    if answer < 0: answer *= -1
    return answer