def user_choice():
    choice = "WRONG"
    while (choice.isdigit() == False):
        choice = input("Please enter a number (0-10): ")

        if (choice.isdigit() == False):
            print("Sorry that is not a digit!")

    return int(choice)


some_value = "100"
print(f"1: {some_value}")
print(f"2: {some_value.isdigit()}")
result = user_choice()
print(f"3: {result}")


def user_choice2():
    choice = "WRONG"
    acceptable_range = range(0, 10)
    within_range = False

    while (choice.isdigit() == False or within_range == False):
        choice = input("Please enter a number (0-10): ")

        if (choice.isdigit() == False):
            print("Sorry that is not a digit!")

        if (choice.isdigit()) == True:
            if (int(choice) in acceptable_range):
                within_range = True
            else:
                print("Sorry, you are out of acceptable range (0-10)")
                within_range = False

    return int(choice)


result = "WRONG VALUE"
accepted_values = [0, 1, 2]
print(f"4: {result in accepted_values}")
print(f"5: {result not in accepted_values}")
result = user_choice2()
print(f"6: {result}")
