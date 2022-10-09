my_file = open("my_file.txt", "w+")
my_file.write(
    "Hello this is a text file\nthis is the second line\nthis is the third line")
my_file.seek(0)
print(f"1: {my_file.read()}")
my_file.seek(0)
print(f"2: {my_file.readlines()}")
with open("my_new_file.txt", mode="w+") as my_file_new:
    my_file_new.write("this is the first line\n")
    my_file_new.write("this is the second line")
    my_file_new.seek(0)
    contents = my_file_new.read()
    print(f"3: {contents}")
