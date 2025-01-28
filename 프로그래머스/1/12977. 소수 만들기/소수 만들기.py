def solution(nums):
    
    def CheckIsPrimeNumber(num):
        for l in range(2, int(num**0.5)+1):
            if num%l == 0:
                return False
        return True

    result = 0
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if CheckIsPrimeNumber(sum((nums[i], nums[j], nums[k]))):
                    result += 1
                else: pass
    
    answer = result

    return answer