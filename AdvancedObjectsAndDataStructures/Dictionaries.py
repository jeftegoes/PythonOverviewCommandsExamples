d = {"k1": 1, "k2": 2}
my_dict = {x: x**2 for x in range(10)}
print(f"1: {my_dict}")

my_dict = {k: v**2 for k, v in zip(["a", "b"], range(2))}
print(f"2: {my_dict}")
for k, v in my_dict.items():
    print(f"3: Key: {k} Value: {v}")
print(f"4: {my_dict.items()}")
