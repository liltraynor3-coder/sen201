
from models import Book, User

class LibrarySystem:
    def __init__(self):
        self.books = {}
        self.users = {}

    def add_book(self, book_id, title, author):
        self.books[book_id] = Book(book_id, title, author)

    def add_user(self, user_id, name):
        self.users[user_id] = User(user_id, name)

    def issue_book(self, book_id):
        if book_id in self.books and not self.books[book_id].is_issued:
            self.books[book_id].is_issued = True
            return True
        return False

    def return_book(self, book_id):
        if book_id in self.books and self.books[book_id].is_issued:
            self.books[book_id].is_issued = False
            return True
        return False

    def view_books(self):
        return self.books
