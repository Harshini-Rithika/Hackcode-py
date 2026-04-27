import calendar
import datetime
user_input = input().split()
month = int(user_input[0])
day = int(user_input[1])
year = int(user_input[2])
weekday_index = calendar.weekday(year, month, day)
day_name = calendar.day_name[weekday_index]
print(day_name.upper())