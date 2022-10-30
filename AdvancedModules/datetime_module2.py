from datetime import date, datetime

my_date_time = datetime(2021, 10, 3, 14, 20, 1)
print(f"1: {my_date_time}")

my_date_time = my_date_time.replace(year=2022)
print(f"2: {my_date_time}")

date1 = date(2022, 11, 3)
date2 = date(2021, 11, 3)
date_diff = date1 - date2
print(f"3: {type(date_diff)}")
print(f"4: {date_diff.days}")

datetime1 = datetime(2022, 11, 3, 22, 0)
datetime2 = datetime(2021, 11, 3, 12, 0)
datetime_diff = datetime1 - datetime2
print(f"5: {datetime_diff.seconds}")
print(f"6: {datetime_diff.total_seconds()}")
print(f"7: {datetime_diff}")
