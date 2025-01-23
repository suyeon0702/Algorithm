left_ps, right_ps = "(", ")"
t = int(input())
for i in range(t):
    stack = []
    result = "YES"

    # ps_string 계산
    ps_string = input()
    for j in range(len(ps_string)):
        ps = ps_string[j]

        # 왼쪽 괄호일 경우 stack에 추가
        if ps == left_ps: 
            stack.append(ps)
        # 오른쪽 괄호일 경우 stack에서 왼쪽 괄호 하나 제거
        elif ps == right_ps: 
            if len(stack) == 0: # stack에 남은 왼쪽 괄호가 없는 경우 -> NO
                result = "NO"
            else:
                stack.pop()

    # 다 끝나고 왼쪽 괄호가 스택에 남아있는 경우 -> NO
    if len(stack) > 0: 
        result = "NO"

    # 결과 출력
    print(result)
