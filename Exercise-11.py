# 1

class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, page):
        self.author = author
        self.page = page
        super().__init__(name)

    def print_info(self):
        print(f"Name is: {self.name}, Author is: {self.author}, Page count is: {self.page}")


class Magazine(Publication):
    def __init__(self, name, chief):
        self.chief = chief
        super().__init__(name)

    def print_info(self):
        print(f"Name is: {self.name}, chief is: {self.chief})")


book = Book("Campartment No. 6", "Rosa Liksom", 192)
magazine = Magazine("Donald Duck", "Aki Hyppa")

book.print_info()
magazine.print_info()