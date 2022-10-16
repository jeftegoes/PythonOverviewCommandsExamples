def create_cubes(n: int):
    result = []
    for x in range(n):
        result.append(x**3)
    return result


def create_cubes_yield(n: int):
    for x in range(n):
        yield x**3


print(f"1: {create_cubes(10)}")
for x in create_cubes(10):
    print(x)
print(f"2: {create_cubes}")

for x in create_cubes_yield(10):
    print(f"3: {x}")
    
print(f"4: {create_cubes_yield}")
print(f"5: {list(create_cubes_yield(10))}")


def generate_fibonacci(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b

for number in generate_fibonacci(10):
    print(f"6: {number}")
