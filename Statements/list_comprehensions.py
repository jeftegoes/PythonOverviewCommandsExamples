my_string = "Hello"

my_list = []

for letter in my_string:
    my_list.append(letter)

print(f"1: {my_list}")

my_list = [letter for letter in my_string]
print(f"2: {my_list}")

my_list = [x for x in "word"]
print(f"3: {my_list}")

my_list = [num for num in range(0, 11)]
print(f"4: {my_list}")

my_list = [num**2 for num in range(0, 11)]
print(f"5: {my_list}")

my_list = [num**2 for num in range(0, 11) if num % 2 == 0]
print(f"6: {my_list}")

celcius = [0, 10, 20, 34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]

print(f"7: {fahrenheit}")

fahrenheit = []
for temp in celcius:
    fahrenheit.append(((9/5)*temp + 32))

print(f"8: {fahrenheit}")

results = [x if x % 2 == 0 else "ODD" for x in range(0, 11)]
print(f"9: {results}")

my_list = []
for x in [2, 4, 6]:
    for y in [1, 10, 1000]:
        my_list.append(x*y)

print(f"10: {my_list}")

my_list = [x*y for x in [2, 4, 6] for y in [1, 10, 1000]]
print(f"11: {my_list}")
