import re

text = "The agent's phone number is 408-555-1234. Call soon!"
print(f"1: {'phone' in text}")

pattern = "not in text"
print(f"2: {re.search(pattern, text)}")

pattern = "phone"
match = re.search(pattern, text)
print(f"3: {match}")

print(f"4: {match.span()}")
print(f"5: {match.start()}")
print(f"6: {match.end()}")

text = "My phone once, my phone twice"
match = re.search("phone", text)
print(f"7: {match.span()}")

matches = re.findall("phone", text)
print(f"8: {matches}")

for match in re.finditer("phone", text):
    print(f"9: {match}")
    print(f"10: {match.span()}")
