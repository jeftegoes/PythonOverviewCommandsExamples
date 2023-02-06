class BookShelf:
    def __init__(self, *books) -> None:
        self.books = books

    def __str__(self) -> str:
        for book in self.books:
            print(f"{book}")

        return f"BookShelf with {len(self.books)} books."


class Book:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"Book: {self.name}"


book1 = Book("Capitães da Areia")
book2 = Book("Python 101")

bookShelf = BookShelf(book1, book2)

print(bookShelf)
