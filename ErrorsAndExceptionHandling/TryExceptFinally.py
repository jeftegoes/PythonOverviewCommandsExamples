def add(n1, n2):
    print(n1+n2)


add(10, 20)

number1 = 10
number2 = input("Please provide a number: ")
# add(number1, number2)
print("Sommenthing happened!")

try:
    result = 10 + "10"
except TypeError:
    print("Hey it look like you aren't adding correctly!")
else:
    print("Add went well!")
    print(result)


try:
    result = 20 + 20
except:
    print("Hey it look like you aren't adding correctly!")
else:
    print("Add went well!")
    print(result)

try:
    f = open("testfile", "r")
    f.write("Write a test line.")
except TypeError:
    print("There was a type error!")
except OSError:
    print("Hey you have an OS Error.")
except:
    print("All other exceptions!")
finally:
    print("I always run")


def ask_for_int():
    while True:
        try:
            result = int(input("Please provide number: "))
        except:
            print("Whoops! That is not a number.")
            continue
        else:
            print("Yes thank you.")
            break
        finally:
            print("I'm going to ask you again!\n")


ask_for_int()
