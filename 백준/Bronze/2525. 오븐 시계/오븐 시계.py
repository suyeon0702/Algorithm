h, m = map(int, input().split(' '))
cook_time = int(input()) # minute
# 분 계산
total_minute = m + cook_time
finish_minute = total_minute % 60
plus_hour = total_minute // 60
# 시 계산
total_hour = h + plus_hour
finish_hour = total_hour % 24
print(finish_hour, finish_minute)