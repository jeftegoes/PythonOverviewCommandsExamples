stock_prices = [("Appl", 200), ("Goog", 400), ("Msft", 100)]
for item in stock_prices:
    print(f"1: {item}")

for ticker, price in stock_prices:
    print(f"2: {price+(0.1*price)}")


def employee_check(work_hours):
    current_max = 0
    employee_of_month = ""

    for employee, hours in work_hours:
        if (hours > current_max):
            current_max = hours
            employee_of_month = employee
        else:
            pass

    return (employee_of_month, current_max)


work_hours = [("Abby", 100), ("Billy", 400), ("Cassie", 800)]
print(f"3: {employee_check(work_hours)}")

name, hours = employee_check(work_hours)
print(f"4: {name}")
print(f"5: {hours}")
