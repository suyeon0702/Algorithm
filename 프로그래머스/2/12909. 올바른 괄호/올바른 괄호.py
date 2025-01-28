def solution(s):
    left_ps = "("
    right_ps = ")"
    answer = True
    
    ps_list = []
    for ps in s:
        if ps == left_ps:
            ps_list.append(ps)
        elif ps == right_ps:
            if len(ps_list) == 0: # 오른쪽 괄호에 상응하는 왼쪽 괄호가 없을 때
                answer = False
                break
            else: ps_list.pop()
    # 반복 종료 후 왼쪽 괄호가 남았을 때
    if len(ps_list) != 0:
        answer = False

    return answer