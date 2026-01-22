
from library import LibrarySystem

def main():
    library = LibrarySystem()

    library.add_book(1, "Python Basics", "Guido van Rossum")
    library.add_book(2, "Software Engineering", "Ian Sommerville")

    library.add_user(1, "Alice")

    library.issue_book(1)
    library.return_book(1)

    books = library.view_books()
    for book in books.values():
        status = "Issued" if book.is_issued else "Available"
        print(book.title, "-", status)

if __name__ == "__main__":
    main()
