import re

print(f"1: {re.search(r'cat|dog', 'The cat is here.')}")
print(f"2: {re.findall(r'...at', 'The cat in the hat went splat.')}")
result = re.findall(r'\d', 'The number is 2.')
print(f"3: {result}")

phrase = "There are 3 numbers 34 inside 5 this sentence"
pattern = r"[^\d]+"
print(f"4: {re.findall(pattern, phrase)}")

phrase = "This is a string! But it has punctuation. How can we remove it?"
pattern = r"[^!.?]+"
print(f"5: {re.findall(pattern, phrase)}")

phrase = "This is a string! But it has punctuation. How can we remove it?"
pattern = r"[^!.? ]+"
result = re.findall(pattern, phrase)
print(f"6: {result}")
print(f"7: {' '.join(result)}")
