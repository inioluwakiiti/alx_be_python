class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return True
        else:
            return False

    def return_book(self):
        self.is_available = True

    def show_info(self):
        status = "Available" if self.is_available else "Borrowed"
        print(f"{self.title} by {self.author} | {status}")


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"{book.title} is not available right now.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} does not have this book.")

    def show_info(self):
        print(f"{self.name} (ID: {self.member_id})")


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book.title}")

    def add_member(self, member):
        self.members.append(member)
        print(f"New member added: {member.name}")

    def show_books(self):
        if not self.books:
            print("No books in the library yet.")
        else:
            print("Books in library:")
            for book in self.books:
                book.show_info()

    def show_members(self):
        if not self.members:
            print("No members registered yet.")
        else:
            print("Library Members:")
            for member in self.members:
                member.show_info()

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
