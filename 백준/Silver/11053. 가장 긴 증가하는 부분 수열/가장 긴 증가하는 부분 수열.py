N = int(input())
A = list(map(int, input().split()))

def binary_search(arr, target): # 목표 값과 같은 위치(첫 번째), 목표값보다 큰 위치(첫 번째)
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] >= target: # 목표값 <= 중간값
            right = mid
        else: # 중간값 < 목표값
            left = mid + 1

    return left # 최종 위치 반환

sub_A = []

for num in A:
    pos = binary_search(sub_A, num)
    
    if pos < len(sub_A):
        sub_A[pos] = num
    else:
        sub_A.append(num)

print(len(sub_A))