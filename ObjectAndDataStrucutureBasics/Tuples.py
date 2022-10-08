t = (1, 2, 3)
my_list = [1, 2, 3]
print(f"1: {type(t)}")
print(f"2: {type(my_list)}")
print(f"3: {len(t)}")
t = ("one", 2)
print(f"4: {t[0]}")
print(f"5: {t[-1]}")
t = ("a", "a", "b")
print("6: {}".format(t.count("a")))
print("7: {}".format(t.index("a")))
print("8: {}".format(t.index("b")))
my_list[0] = "NEW"
print(f"9: {my_list}")
# t[0] = "NEW" <<< TypeError: 'tuple' object does not support item assignment
