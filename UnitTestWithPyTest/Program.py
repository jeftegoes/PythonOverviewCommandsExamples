def sum_values(a, b):
    try:
        return a + b
    except TypeError:
        return f"Invalid input."


print(sum_values(10, 20))
