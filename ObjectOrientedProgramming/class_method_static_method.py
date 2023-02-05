class ClassTest:
    static_attribute_here = "4: Static attribute here."

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

    def __init__(self, name, book_type, weight) -> None:
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPES[0], page_weight + 100)

    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPES[1], page_weight)

    def this_is_same_classmethod(self, name, page_weight):
        return Book(name, Book.TYPES[1], page_weight)


book = Book.hardcover("Harry Potter", 1500)
light = Book.hardcover("Python 101", 600)
test = Book.this_is_same_classmethod("Python 101", 600)

print(book)
print(light)
print(test)