import sys

mixed_string = sys.stdin.readline()
upsidedown = ""
for alp in mixed_string:
    if alp == alp.upper(): # 대문자
        upsidedown += alp.lower() # 소문자로
    else: # 소문자
        upsidedown += alp.upper() # 대문자
print(upsidedown)