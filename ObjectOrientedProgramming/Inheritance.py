class Animal():
    def __init__(self):
        print(f"1: Animal created.")

    def who_am_i(self):
        print(f"4: am an animal.")

    def eat(self):
        print(f"3: am eating.")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print(f"2: Dog created.")

    def who_am_i(self):
        print(f"4: am a dog!")


animal = Animal()
dog = Dog()
dog.eat()
dog.who_am_i()
