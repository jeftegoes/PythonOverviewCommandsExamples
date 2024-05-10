from random import randint, shuffle

for num in range(10):
    print(f"1: {num}")

for num in range(3, 10):
    print(f"2: {num}")

for num in range(0, 11, 2):
    print(f"3: {num}")

my_list = list(range(0, 11, 2))
print(f"4: {my_list}")

index_count = 0
for letter in "abcde":
    print("5: At index {0} the letter is {1}".format(index_count, letter))
    index_count += 1


index_count = 0
word = "abcde"
for letter in word:
    print(f"6: { word[index_count] }")
    index_count += 1


for index, letter in enumerate(word):
    print(f"7: Index: { index } Letter: { letter }")

my_list_1 = [1, 2, 3]
my_list_2 = ["a", "b", "c"]
my_list_3 = [100, 200, 300]
for item in zip(my_list_1, my_list_2, my_list_3):
    print(f"8: {item}")

my_list = list(zip(my_list_1, my_list_2))
print(f"9: {my_list}")

my_dictionary = {'mykey': 345}

print(f"10: { 'x' in [1, 2, 3] }")
print(f"11: { 'x' in ['x', 'y', 'z'] }")
print(f"12: { 'a' in 'a world' }")
print(f"13: { 'mykey' in my_dictionary }")
print(f"14: { 345 in my_dictionary.keys() }")

my_list = [10, 20, 30, 40, 100]
print(f"15: { min(my_list) }")
print(f"16: { max(my_list) }")

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(my_list)
print(f"17: { my_list }")
print(f"18: { randint(0, 100) }")
result = input("Favorite number: ")
print(f"19: { type(result) }")
print(f"20: { type(int(result)) }")
