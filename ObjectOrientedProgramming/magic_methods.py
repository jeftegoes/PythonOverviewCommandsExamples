class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    # def __str__(self) -> str:
    #     return f"Person {self.name}, {self.age} years old."

    def __repr__(self) -> str:
        return f"<Person('{self.name}', {self.age})>"


jefte = Person("Jefté", 31)
print(jefte)
