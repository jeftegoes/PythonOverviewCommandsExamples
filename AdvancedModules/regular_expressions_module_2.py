import re

text = "My phone number is 408-555-1234"
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)
print(f"1: {phone}")
print(f"2: {phone.group()}")

phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
print(f"3: {phone}")
print(f"4: {phone.group()}")

phone_pattern = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
results = re.search(phone_pattern, text)
print(f"5: {results}")
print(f"6: {results.group(1)}")
print(f"7: {results.group(2)}")
print(f"8: {results.group(3)}")
