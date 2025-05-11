class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.__isbn = isbn
        self.available = available

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.__isbn}")
        print(f"Available: {'Yes' if self.available else 'No'}")

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, isbn):
        self.__isbn = isbn


class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.__membership_id = membership_id
        self.borrowed_books = []

    def get_membership_id(self):
        return self.__membership_id

    def set_membership_id(self, membership_id):
        self.__membership_id = membership_id

    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed a book.")
        else:
            print(f"Sorry, a book is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned a book.")
        else:
            print(f"Error: {self.name} did not borrow a book.")


class StaffMember(Member):
    def __init__(self, name, membership_id, staff_id):
        super().__init__(name, membership_id)
        self.staff_id = staff_id

    def add_book(self, library, book):
        if isinstance(library, Library):
            library.add_book_to_collection(book)
            print(f"Staff member {self.name} (ID: {self.staff_id}) added a book to the library.")
        else:
            library.append(book)
            print(f"Staff member {self.name} (ID: {self.staff_id}) added a book to the collection.")


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book_to_collection(self, book):
        self.books.append(book)
        print(f"A book added to the library collection.")

    def display_all_books(self):
        if not self.books:
            print("The library has no books.")
            return
        print("\n--- Library Books ---")
        for book in self.books:
            book.display_info()
            print("--------------------")

# usage example
print("--- Demonstrating Class Usage ---")

book1 = Book("Book Title 1", "Author Name 1", "978-0321765723")
book2 = Book("Book Title 2", "Author Name 2", "978-0132350884", available=False)

print("\nDisplaying Book Info:")
book1.display_info()
print("-" * 20)
book2.display_info()
print("-" * 20)

member1 = Member("Member One", "M001")
staff1 = StaffMember("Staff One", "S001", "STF001")

library = Library()

staff1.add_book(library, book1)
staff1.add_book(library, book2)

library.display_all_books()

member1.borrow_book(book1)
member1.borrow_book(book2) 

print("\nDisplaying Book Info After Borrowing:")
book1.display_info()
print("-" * 20)
book2.display_info()
print("-" * 20)

member1.return_book(book1)
member1.return_book(book2) # Try returning a book not borrowed

print("\nDisplaying Book Info After Returning:")
book1.display_info()
print("-" * 20)
book2.display_info()
print("-" * 20)

print("\n--- Demonstration Complete ---")
