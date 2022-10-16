def simple_gen():
    for x in range(3):
        yield x


for number in simple_gen():
    print(number)

g = simple_gen()
print(f"1: {g}")
print(f"2: {next(g)}")
print(f"3: {next(g)}")
print(f"4: {next(g)}")
