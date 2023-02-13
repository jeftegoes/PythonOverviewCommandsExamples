from person import Person


def increment(number: int) -> None:
    number += 10


def make_old(person: Person) -> None:
    person.age += 10


first_number = 10
print(f"1: {first_number}")
increment(first_number)
print(f"2: {first_number}")

person = Person(50)
print(f"3: {person.age}")
make_old(person)
print(f"4: {person.age}")