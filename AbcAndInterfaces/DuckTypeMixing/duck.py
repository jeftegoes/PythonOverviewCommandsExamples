from duck_interface import DuckInterface


class Duck(DuckInterface):
    def __init__(self) -> None:
        pass

    def walk(self):
        print("Duck is walking.")

    def swin(self):
        print("Duck is swimming.")

    def quack(self):
        print("Duck is speaking: quack! quack!")
