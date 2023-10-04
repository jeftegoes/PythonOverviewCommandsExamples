from duck_interface import DuckInterface


class Person(DuckInterface):
    def __init__(self) -> None:
        pass

    def walk(self):
        print("The person is walking imitating a duck.")

    def swin(self):
        print("The person can swim imitating a duck.")

    def quack(self):
        print("The person say quack imitating a duck.")
