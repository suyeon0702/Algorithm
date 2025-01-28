def CheckIsPalindrome(num):
    str_num = str(num)
    if str_num == str_num[::-1] : return True
    else: return False

def CheckIsPrime(num):
    if num == 1: return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0: return False
    return True

n = int(input())

result = 0
while 1:
    if CheckIsPalindrome(n) and CheckIsPrime(n):
        result = n
        break
    n+=1
print(result)