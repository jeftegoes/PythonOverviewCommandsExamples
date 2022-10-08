my_dict = {"key1": "value1", "key2": "value2"}
print(f"1: {my_dict}")
print("2: {}".format(my_dict["key1"]))
prices_lookup = {"apple": 2.99, "oranges": 1.99, "milk": 5.80}
print("3: {}".format(prices_lookup["apple"]))
d = {"k1": 123, "k2": [0, 1, 2], "k3": {"insideKey": 100}}
print("4: {}".format(d["k2"]))
print("5: {}".format(d["k3"]["insideKey"]))
d = {"key1": ["a", "b", "c"]}
print("6: {}".format(d))
my_list = d["key1"]
print(f"7: {my_list}")
letter = my_list[2]
print(f"8: {letter}")
print(f"9: {letter.upper()}")
print("10: {}".format(d["key1"][2].upper()))
d = {"k1": 100, "k2": 200}
print(f"11: {d}")
d["k3"] = 300
print(f"13: {d}")
d["k1"] = "NEW VALUE"
print(f"14: {d}")
print(f"15: {d.values()}")
print(f"16: {d.items()}")
