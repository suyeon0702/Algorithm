while 1:
    a, b = map(int, input().split(' '))

    if a == 0 and b == 0:
        break

    # a = b = 0 외에는 a와 b가 같은 경우는 없다
    # a는 b의 약수 -> factor
    # a는 b의 배수 -> multiple
    # a는 b의 약수도 배수도 아님 -> neither

    # 0일 경우 나눌 수 없으므로 예외처리
    if a == 0 or b == 0:
        print("neither")
    else:
        if max(a, b) % min(a, b) == 0:
            if a < b: print("factor")
            else: print("multiple")
        else:
            print("neither")
    
