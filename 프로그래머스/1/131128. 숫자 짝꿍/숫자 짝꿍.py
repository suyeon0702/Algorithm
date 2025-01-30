def solution(X, Y):
    if len(X) < len(Y):
        num1, num2 = X, Y
    else:
        num1, num2 = Y, X
        
    num1_list = [0 for _ in range(10)]
    common_num_list = [0 for _ in range(10)]
    # num1 구성 정리
    for n in num1:
        num1_list[int(n)] += 1
    # num2와 일치하는 수 찾기
    for n in num2:
        if num1_list[int(n)] > 0:
            common_num_list[int(n)] += 1
            num1_list[int(n)] -= 1
        else: pass
    # 가장 큰 짝꿍 수 찾기
    answer = ''
    if sum(common_num_list) == 0: # 공통 숫자가 없는 경우
        answer = '-1'
    elif common_num_list[0] == sum(common_num_list): # 0 밖에 없는 경우
        answer = '0'
    else:
        for i in range(9, -1, -1):
            str_num = str(i) * common_num_list[i]
            answer += str_num

    return answer