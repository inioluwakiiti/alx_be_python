class Book:
  def __init__
    self.title = title
    self.author = author
    self._is_checked_out = False

def check_out(self):
    self._is_checked_out = True

def return_book(self):
    self._is_checked_out = False

class Library:
def __init__(self):
    self._books=[]

def add_book(self, book):
    self._books.append9book)

def check_out_book(self, title):
   for book in self._books:
     if book.title == title and not book._is_checked_out:
       book.check_out()
       print (f"Checked out: {title}")
       return
print(f"Could not check out '{title}'. It might be unavailable or not exist")

def return_book(self, title):
   for book in self._books:
    if book.title == title and book._is-checked_out:
      book.return_book()
      print(f"Returned:{title}")
      return
print(f"Could not return '{title}'. It might be available or not exist.")

def list_available_books(self):
   available_found = False
   print("Available books:")
   for book in self._books:
     if not book._is_checked_out:
       print(f"{book.title} by {book author}")
       available_found = True

if not available_found and not self._books:
    print("The library is empty.")
