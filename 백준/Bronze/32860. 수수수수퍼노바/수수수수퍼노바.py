# 알파벳 리스트 만들기(소문자)
start_ascii_num = ord("a")
alp_list = ["" for _ in range(26)]
for i in range(26):
    alp_list[i] = chr(start_ascii_num+i)

# 입력
year, m = map(int, input().split(' '))
code = ""

# 1~26번째
if m < 27:
    alp_num = alp_list[m-1].upper()
    code = alp_num
else: # 27~번째
    # Z 다음이 aa이기 때문에 규칙이 달라짐 
    # M <= 702 => 세자리수는 고려 X

    # 나머지가 0인 경우는 앞자리 예외처리 필요
    if m % 26 == 0: # az, bz, cz, ..., zz
        alp_num00 = alp_list[(m-1)//26-1]
    else:
        alp_num00 = alp_list[m//26-1]

    alp_num0 = alp_list[m%26-1]
    code = alp_num00+alp_num0

sn_name = f"SN {year}{code}"
print(sn_name)