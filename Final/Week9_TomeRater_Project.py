# TOME RATER PROJECT
# CLASSES:
class User:  # Methods Tested
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):  # Returns email associated with the user
        return self.email

    def change_email(self, address):  # Takes in a new email and changes the email associated with the user
        self.email = address
        print("This user's email has been updated")

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):  # Calculates average rating
        total_ratings = 0
        for rating in self.books.values():
            if rating:
                total_ratings += rating
        return total_ratings / len(self.books)  # Divide total_ratings by the number of books in dictionary

    def __repr__(self):  # Returns a string to print out this user object in a meaningful way.
        return "User: {},  Email: {},  Books Read: {}.".format(self.name, self.email, len(self.books))

    def __eq__(self, other_user):  # Returns True if name & email match, else False
        return self.name == other_user.name and self.email == other_user.email


class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []  # Instance variable as empty list

    def __repr__(self):
        return "{}, ISBN: {}".format(self.title, self.isbn)

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        print("This book's ISBN has been updated.")  # Should also print a message saying the book's ISBN was updated

    def add_rating(self, rating):  # Adds to Rating List if between 0-4, else prints invalid
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def get_average_rating(self):
        return sum(self.ratings) / len(self.ratings)

    def __hash__(self):  # Allows the book to be hashable. https://docs.python.org/3/library/functions.html#hash
        return hash((self.title, self.isbn))

    def __eq__(self, other_book):  # Returns True if title & isbn match, else False
        return self.title == other_book.title and self.isbn == other_book.isbn


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author  # String

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{} by {}".format(self.title, self.author)


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{}, a {} manual on {}".format(self.title, self.level, self.subject)


class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def __repr__(self):
        return "{} users have read {} books".format(len(self.users), len(self.books))

    def __eq__(self, other_object):  # Returns True if title match, else False
        return self.title == other_object.title

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        user = self.users.get(email, None)
        if user:
            user.read_book(book, rating)
            if rating is not None:
                book.add_rating(rating)
            if book not in self.books:  # If book not in self.books, add to self.books with read count of 1
                self.books[book] = 1
            else:                       # Else, the book already exists in self.books so increase read count by 1
                self.books[book] += 1
        else:
            print("No user with email {}!".format(email))

    def add_user(self, name, email, user_books=None):
        user = User(name, email)
        self.users[email] = user
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books:
            print(book)

    def print_users(self):
        for user in self.users:
            print(user)

    def get_most_read_book(self):  # Returns the highest value found in the dictionary
        highest_value = 0
        highest_key = ""
        for book in self.books:
            if self.books.get(book) > highest_value:
                highest_value = self.books.get(book)
                highest_key = book
        return "Most read book: {}, Read {} times.".format(highest_key, highest_value)

    def highest_rated_book(self):
        highest_value = 0
        book_name = ""
        for book in self.books:
            if book.get_average_rating() > highest_value:
                highest_value = book.get_average_rating()
                book_name = book.title
        return "Highest rated book: {}, Rated at {}.".format(book_name, highest_value)

    def most_positive_user(self):
        highest_value = 0
        user_name = ""
        for user in self.users.values():
            temp_user = user.get_average_rating()
            if temp_user > highest_value:
                highest_value = temp_user
                user_name = user.name
        return "Most postive user: {}, has an average rating of {}.".format(user_name, highest_value)
