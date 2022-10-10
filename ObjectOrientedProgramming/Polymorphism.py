class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError(
            f"1: Subclass must implment this abstract method.")


class Dog(Animal):
    def speak(self):
        return self.name + " says woof!"


class Cat(Animal):
    def speak(self):
        return self.name + " says meow!"


niko = Dog("niko")
felix = Cat("felix")

print(f"1: {niko.speak()}")
print(f"2: {felix.speak()}")

for pet in [niko, felix]:
    print(f"3: {type(pet)}")
    print(f"4: {pet.speak()}")
