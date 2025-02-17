import sys
N = int(sys.stdin.readline().strip())
print("Gnomes:")
for i in range(N):
    is_ordered = True
    beard_list = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(len(beard_list)-2):
        b1, b2, b3 = beard_list[j], beard_list[j+1], beard_list[j+2]
        gap1, gap2 = b1-b2, b2-b3
        if gap1*gap2 < 0:
            is_ordered = False
            break
    if is_ordered: print("Ordered")
    else: print("Unordered")