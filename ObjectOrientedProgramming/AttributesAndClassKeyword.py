my_list = [1, 2, 3]
print(f"1: {type(my_list)}")
my_set = set()
print(f"2: {type(my_set)}")


class Sample():
    pass


class Dog():
    # Class object attribute.
    # Same for any instance of a class.
    species = "mammal"

    def __init__(self, breed, name, spots):
        # Attributes.
        # We take in the argument.
        # Assign it using self.attribute_name.
        self.breed = breed
        self.name = name
        self.spots = spots

    # Operations/Actions -> Methods
    def bark(self, number):
        print("6: WOOF! My name is {0} and the number is {1}.".format(
            self.name, number))


my_sample = Sample()
print(f"3: {type(my_sample)}")

my_dog = Dog("Lab", "Sammy", "NO SPOTS")
print(f"4: {type(my_dog)}")
print(
    f"5: Name: {my_dog.name} Breed: {my_dog.breed} Spots: {my_dog.spots} Specie: {my_dog.species}.")
my_dog.bark(10)
print(f"7: {my_dog.bark}")


class Circle():
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius*radius*self.pi

    def get_circumference(self):
        return self.radius * self.pi * 2


my_circle = Circle(30)
print(f"8: {my_circle.pi}")
print(f"9: {my_circle.radius}")
print(f"10: {my_circle.area}")
print(f"11: {my_circle.get_circumference()}")
