small_a_ord = ord('a') # 97
n = int(input())
log = input()
alp_stack = []
stable = 1
for alp in log:
    if ord(alp) >= small_a_ord: # 소문자
        alp_stack.append(alp)
    else: # 대문자
        if len(alp_stack) == 0:
            stable = 0
            break
        else:
            last = alp_stack[-1]
            if alp.lower() == last:
                alp_stack.pop()
            else:
                stable = 0
                break
if len(alp_stack) != 0:
    stable = 0

print(stable)