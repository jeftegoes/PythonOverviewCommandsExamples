from collections import Counter, defaultdict, namedtuple

my_list = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3]
print(f"1: {Counter(my_list)}")


my_list = ["a", "a", 10, 10, 10]
print(f"2: {Counter(my_list)}")

print(f"3: {Counter('aaaaaabbbbbbsdhdh')}")

sentence = "How many times does each word show up in this setence with a word"
print(f"4: {sentence.split()}")

print(f"5: {Counter(sentence.split())}")

letters = "aaabbbbcccccccccdddddddd"
c = Counter(letters)
print(f"6: {c}")
print(f"7: {c.most_common()}")
print(f"8: {c.most_common(2)}")

d = defaultdict(lambda: 0)
d['a'] = 10
print(f"9: {d}")
print(f"10: {d['a']}")
print(f"11: {d['wrong']}")
print(f"12: {d}")


my_tuple = (10, 20, 30)
print(f"13: {my_tuple[0]}")

Dog = namedtuple("Dog", ["age", "breed", "name"])
sammy = Dog(age=5, breed="Husky", name="Sam")

print(f"14: {type(sammy)}")
print(f"15: {sammy}")
print(f"16: {sammy.age}")
print(f"17: {sammy.name}")
