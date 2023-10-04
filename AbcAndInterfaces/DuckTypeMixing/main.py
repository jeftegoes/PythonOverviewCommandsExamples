from duck import Duck
from duck_interface import DuckInterface
from person import Person

person = Person()
duck = Duck()

list_of_ducks: list[DuckInterface] = [person, duck]

for duck in list_of_ducks:
    duck.walk()
    duck.swin()
    duck.quack()