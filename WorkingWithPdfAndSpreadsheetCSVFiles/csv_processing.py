import csv

csv_file = open("example.csv", encoding="utf-8")
csv_data = csv.reader(csv_file)
data_lines = list(csv_data)
print(f"1: {data_lines}")
print(f"2: {len(data_lines)}")

for line in data_lines[:3]:
    print(f"3: {line}")

for line in data_lines[1:]:
    print(f"4: {line}")

all_emails = []
for line in data_lines[1:]:
    all_emails.append(line[3])

print(f"5: {all_emails}")


full_names = [f"{line[1]} {line[2]}" for line in data_lines[1:]]

print(f"6: {full_names}")

file_to_output = open("to_save_file.csv", mode="w", newline="")
csv_writter = csv.writer(file_to_output, delimiter=",")
csv_writter.writerow(["a", "b", "c"])
csv_writter.writerows([["1", "2", "3"], ["4", "5", "6"]])
file_to_output.close()
