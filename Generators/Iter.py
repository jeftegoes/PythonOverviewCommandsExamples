s = "Hello"
for letter in s:
    print(f"1: {letter}")

s_iter = iter(s)
print(f"2: {next(s_iter)}")
