def solution(ineq, eq, n, m):
    answer = -1
    if n == m:
        answer = int(eq == "=")
    elif n > m:
        answer = int(ineq == ">")
    elif n < m:
        answer = int(ineq == "<")
    return answer