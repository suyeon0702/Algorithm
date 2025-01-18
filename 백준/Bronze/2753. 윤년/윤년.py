year = int(input())
is_4n = (year%4 == 0)
is_100n = (year%100 == 0)
is_400n = (year%400 == 0)

result = 0
if is_4n:
    if not is_100n or is_400n:
        result = 1

print(result)
