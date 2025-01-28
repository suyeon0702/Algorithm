def DoPlusCicle(str_num):
    a, b = str_num[0], str_num[1]
    c = str(int(a)+int(b))[-1]
    result_str_num = b+c
    return result_str_num

n = int(input())
str_n = '{0:02d}'.format(n)
new_str_n = str_n # param 초기화
call_cnt = 0
while 1:
    new_str_n = DoPlusCicle(new_str_n)
    call_cnt += 1
    if new_str_n == str_n:
        break
print(call_cnt)