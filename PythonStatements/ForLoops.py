my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in my_list:
    print(f"1: {num}")

for num in my_list:
    if num % 2 == 0:
        print(f"2: {num}")
    else:
        print(f"2: {num}")

for letter in "Hello World":
    print(f"3: {letter}")

tup = (1, 2, 3)
for item in tup:
    print(f"4: {item}")

my_list = [(1, 2), (3, 4), (5, 6), (7, 8)]
print(f"5: {len(my_list)}")

for item in my_list:
    print(f"6: {item}")

my_list = [(1, 2, 3), (5, 6, 7), (8, 9, 10)]

for a, b, c in my_list:
    print(f"7: First: {a} Second: {b} Thrid: {c}")

my_dictionary = {"k1": 1, "k2": 2, "k3": 3}
for key, value in my_dictionary.items():
    print(f"8: Key: {key} Value: {value}")

for key in my_dictionary.keys():
    print(f"10: Value: {key}")

for value in my_dictionary.values():
    print(f"9: Value: {value}")
