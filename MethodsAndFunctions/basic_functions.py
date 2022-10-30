def say_hello():
    print("1: Hello")
    print("1: are")
    print("1: you")


say_hello()
print(f"2: {say_hello}")


def say_hello(name: str = "Default"):
    print(f"3: Hello {name}")


say_hello("Jefté")
say_hello()


def add_num(num1: int, num2: int):
    return num1+num2


print(f"4: {add_num(10, 20)}")
