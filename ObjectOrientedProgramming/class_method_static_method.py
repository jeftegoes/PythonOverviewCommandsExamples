class ClassTest:
    static_attribute_here = "4: Static attribute here."

    def __init__(self) -> None:
        self.name = "Local variable."

    def instance_method(self):
        print(f"1: Called instance_method of {self}.")

    @classmethod
    def class_method(cls):
        print(f"2: Called class_method of {cls}.")

    @staticmethod
    def static_method(test_parameter):
        print(f"3: Called static_method: {test_parameter}")


class_test = ClassTest()

class_test.instance_method()
ClassTest.instance_method(class_test)
class_test.class_method()

ClassTest.static_method("This is work.")
print(ClassTest.static_attribute_here)


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, book_type: str, weight: int) -> None:
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name: str, page_weight: int) -> "Book":
        return Book(name, Book.TYPES[1], page_weight)


book = Book.hardcover("Captains of the Sands", 1500)
light = Book.paperback("Dona Flor and Her Two Husbands.", 600)

print(book)
print(light)
