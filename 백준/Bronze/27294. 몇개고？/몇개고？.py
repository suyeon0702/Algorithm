t, s = map(int, input().split())

is_lunch = (t >= 12 and t <= 16)

rice = 280
if not s and is_lunch:
    rice = 320
print(rice)