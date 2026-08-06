class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.borrower_id = None  # Stores patron_id when issued

    def __str__(self):
        status = f"Borrowed by Patron #{self.borrower_id}" if self.borrower_id else "Available"
        return f"[{self.book_id}] '{self.title}' by {self.author} — {status}"


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []  # List of book_ids currently borrowed

    def __str__(self):
        return f"Patron ID: {self.patron_id} | Name: {self.name} | Books Held: {len(self.borrowed_books)}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []    # List of Book objects
        self.patrons = []  # List of Patron objects

    # --- Helper Search Methods ---
    def _find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def _find_patron(self, patron_id):
        for patron in self.patrons:
            if patron.patron_id == patron_id:
                return patron
        return None

    # --- Registration & Management ---
    def add_book(self, book_id, title, author):
        if self._find_book(book_id):
            print(f"Error: Book ID {book_id} already exists.")
            return
        self.books.append(Book(book_id, title, author))
        print(f"Added Book: '{title}'")

    def register_patron(self, patron_id, name):
        if self._find_patron(patron_id):
            print(f"Error: Patron ID {patron_id} is already registered.")
            return
        self.patrons.append(Patron(patron_id, name))
        print(f"Registered Patron: {name} (ID: {patron_id})")

    # --- Core Operations ---
    def issue_book(self, book_id, patron_id):
        book = self._find_book(book_id)
        patron = self._find_patron(patron_id)

        if not book:
            print(f"Error: Book ID {book_id} not found.")
            return
        if not patron:
            print(f"Error: Patron ID {patron_id} not registered.")
            return
        if book.borrower_id is not None:
            print(f"Sorry, '{book.title}' is already borrowed.")
            return

        book.borrower_id = patron_id
        patron.borrowed_books.append(book_id)
        print(f"Success: '{book.title}' issued to {patron.name}.")

    def return_book(self, book_id):
        book = self._find_book(book_id)

        if not book:
            print(f"Error: Book ID {book_id} not found.")
            return
        if book.borrower_id is None:
            print(f"Notice: '{book.title}' was not issued.")
            return

        patron = self._find_patron(book.borrower_id)
        if patron and book_id in patron.borrowed_books:
            patron.borrowed_books.remove(book_id)

        print(f"Success: Returned '{book.title}' from Patron #{book.borrower_id}.")
        book.borrower_id = None

    # --- Display Methods ---
    def display_books(self):
        print(f"\n--- {self.name} Book Catalog ---")
        if not self.books:
            print("No books available.")
            return
        for book in self.books:
            print(book)

    def display_patrons(self):
        print(f"\n--- {self.name} Registered Patrons ---")
        if not self.patrons:
            print("No patrons registered.")
            return
        for patron in self.patrons:
            print(patron)


# --- Example Usage ---
if __name__ == "__main__":
    my_library = Library("City Central Library")

    # Register Patrons
    my_library.register_patron(1, "Alice Smith")
    my_library.register_patron(2, "Bob Jones")

    # Add Books
    my_library.add_book(101, "The Hobbit", "J.R.R. Tolkien")
    my_library.add_book(102, "1984", "George Orwell")

    # Display initial state
    my_library.display_books()
    my_library.display_patrons()

    # Issue book to Alice
    my_library.issue_book(101, 1)

    # Try issuing same book to Bob
    my_library.issue_book(101, 2)

    # Display updated state
    my_library.display_books()
    my_library.display_patrons()

    # Return book
    my_library.return_book(101)
    my_library.display_books()



#OUTPUT

'''
Registered Patron: Alice Smith (ID: 1)
Registered Patron: Bob Jones (ID: 2)
Added Book: 'The Hobbit'
Added Book: '1984'

--- City Central Library Book Catalog ---
[101] 'The Hobbit' by J.R.R. Tolkien — Available
[102] '1984' by George Orwell — Available

--- City Central Library Registered Patrons ---
Patron ID: 1 | Name: Alice Smith | Books Held: 0
Patron ID: 2 | Name: Bob Jones | Books Held: 0
Success: 'The Hobbit' issued to Alice Smith.
Sorry, 'The Hobbit' is already borrowed.

--- City Central Library Book Catalog ---
[101] 'The Hobbit' by J.R.R. Tolkien — Borrowed by Patron #1
[102] '1984' by George Orwell — Available

--- City Central Library Registered Patrons ---
Patron ID: 1 | Name: Alice Smith | Books Held: 1
Patron ID: 2 | Name: Bob Jones | Books Held: 0
Success: Returned 'The Hobbit' from Patron #1.

--- City Central Library Book Catalog ---
[101] 'The Hobbit' by J.R.R. Tolkien — Available
[102] '1984' by George Orwell — Available
'''
