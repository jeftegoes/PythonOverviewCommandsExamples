class Book:
    def __init__(self, name: str, page_count: int) -> None:
        self.name = name
        self.page_count = page_count


class BookShelf:
    def __init__(self, books: list[Book]) -> None:
        pass


def list_avg(sequence: list) -> float:
    return sum(sequence) / len(sequence)


books: list[Book] = []
books.append(Book("Captains of the Sands", 120))
books.append(Book("Dona Flor and Her Two Husbands.", 100))

for book in books:
    print(book.name)