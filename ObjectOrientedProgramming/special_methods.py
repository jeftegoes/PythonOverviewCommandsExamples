my_list = [1, 2, 3]
print(f"1: {len(my_list)}")


class Sample():
    pass


my_sample = Sample()
print(f"2: {my_sample}")


class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object has been deleted.")


book = Book("Python", "Yaga", 200)
print(f"3: {book}")
print(f"4: {len(book)}")
del book
print(f"5: {book}")
