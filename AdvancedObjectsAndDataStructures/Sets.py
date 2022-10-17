s = set()
s.add(1)
s.add(2)
print(f"1: {s}")
s.add(2)
print(f"2: {s}")
s.clear()
print(f"3: {s}")
s = {1, 2, 3}
sc = s.copy()
print(f"4: {sc}")
s.add(4)
print(f"5: {s}")
print(f"6: {sc}")
print(f"7: {s.difference(sc)}")
s1 = {1, 2, 3}
s2 = {1, 4, 5}
s1.difference_update(s2)
print(f"8: {s1}")
print(f"9: {s}")
s.discard(2)
print(f"10: {s}")
s1 = {1, 2, 3}
s2 = {1, 2, 5}
print(f"11: {s1.intersection(s2)}")
s1.intersection_update(s2)
print(f"12: {s1}")
s1 = {1, 2}
s2 = {1, 2, 4}
s3 = {5}
print(f"13: {s1.isdisjoint(s2)}")
print(f"14: {s1.isdisjoint(s3)}")
print(f"15: {s1.issubset(s2)}")
print(f"16: {s2.issuperset(s1)}")
print(f"17: {s1.symmetric_difference(s2)}")
print(f"18: {s1.union(s2)}")
s1.update(s2)
print(f"19: {s1}")
