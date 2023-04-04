class Person:
    def __init__(self) -> None:
        print("Chamou aqui 1")

    def __new__(cls):
        print("Chamou aqui 2")
        return super(Person, cls).__new__(cls)
    
    
person1 = Person()
person2 = Person()
print(person1)
print(person2)