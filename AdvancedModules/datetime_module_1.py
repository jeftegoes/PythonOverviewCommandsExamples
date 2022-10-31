import datetime

my_time = datetime.time(13, 20, 1, 20)
print(f"1: {my_time.minute}")
print(f"2: {my_time.hour}")
print(f"3: {my_time}")
print(f"4: {my_time.microsecond}")
print(f"5: {type(my_time)}")
today = datetime.date.today()
print(f"6: {today}")
print(f"7: {today.year}")
print(f"8: {today.month}")
print(f"9: {today.day}")
print(f"10: {today.ctime()}")
