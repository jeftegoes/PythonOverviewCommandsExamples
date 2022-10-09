my_list = [1, 2, 3]
my_list = ["STRING", 100, 23.2]
print(f"1: {len(my_list)}")
my_list = ["one", "two", "three"]
print(f"2: {my_list[0]}")
print(f"3: {my_list[1:]}")
print(f"4: {my_list}")
another_list = ["four", "five"]
print(f"5: {my_list + another_list}")
print(f"6: {another_list}")
new_list = my_list + another_list
print(f"7: {new_list}")
new_list[0] = "ONE ALL CAPS"
print(f"8: {new_list}")
new_list.append("six")
print(f"9: {new_list}")
new_list.append("seven")
print(f"10: {new_list}")
new_list.pop()
print(f"11: {new_list}")
popped_item = new_list.pop()
print(f"12: {new_list}")
new_list.pop(0)
print(f"13: {new_list}")
new_list = ["a", "e", "x", "b", "c"]
num_list = [4, 1, 8, 3]
new_list.sort()
print(f"14: {new_list}")
new_list = ["a", "e", "x", "b", "c"]
my_sorted_list = new_list.sort()
print(f"15: {type(my_sorted_list)}")
print(f"16: {my_sorted_list}")
new_list.sort()
my_sorted_list = new_list
print(f"17: {my_sorted_list}")
num_list.sort()
print(f"18: {num_list}")
num_list.reverse()
print(f"19: {num_list}")
