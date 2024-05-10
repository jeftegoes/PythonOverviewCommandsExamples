x = 0

while x < 5:
    print(f"1: The current value of x is {x}.")
    x += 1
else:
    print("1: X is not lesse than 5.")

x = [1, 2, 3]
for item in x:
    pass

print("2: End of my script.")

my_string = "Sammy"
for letter in my_string:
    if (letter == "a"):
        continue
    print(f"3: {letter}")

for letter in my_string:
    if (letter == "a"):
        break
    print(f"4: {letter}")
    
x = 0
while x < 5:
    if x == 2:
        break
    print(f"5: The current value of x is {x}.")
    x += 1
