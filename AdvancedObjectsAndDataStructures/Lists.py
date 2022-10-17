my_list = [1, 2, 3]
my_list.append(4)
print(f"1: {my_list}")
print(f"2: {my_list.count(1)}")

x = [1, 2, 3]
x.append([4, 5])
print(f"3: {x}")

x = [1, 2, 3]
x.extend([4, 5])
print(f"4: {x}")

l = [1, 2, 3, 4]
print(f"5: {l.index(2)}")

l.insert(2, 'inserted')
print(f"5: {l}")

ele = l.pop()
print(f"6: {ele}")

l.pop(0)
print(f"7: {l}")

l.remove("inserted")
print(f"8: {l}")

l = [1, 2, 3, 4, 3]
l.remove(3)
print(f"9: {l}")

l.reverse()
print(f"9: {l}")
