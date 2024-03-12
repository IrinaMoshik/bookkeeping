class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category

    def __repr__(self):
        return f"{self.title} by {self.author}"

class Shelf:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def sort_books(self):
        self.books.sort(key=lambda x: x.title)

def organize_books(books):
    shelves = {"Shelf 1": Shelf(), "Shelf 2": Shelf(), "Shelf 3": Shelf()}  # Modify as needed based on your shelf structure

    for book in books:
        if book.category == "Classic":
            shelves["Shelf 1"].add_book(book)
        elif book.category == "Fantasy":
            shelves["Shelf 2"].add_book(book)
        else:
            shelves["Shelf 3"].add_book(book)

    for shelf_name, shelf in shelves.items():
        print(f"{shelf_name}:")
        shelf.sort_books()
        for book in shelf.books:
            print(f"\t- {book}")

if __name__ == "__main__":
    # Example books
    books = [
        Book("Pride and Prejudice", "Jane Austen", "Classic"),
        Book("The Hobbit", "J.R.R. Tolkien", "Fantasy"),
        Book("1984", "George Orwell", "Classic"),
        Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "Fantasy"),
        Book("To Kill a Mockingbird", "Harper Lee", "Classic"),
        Book("Dune", "Frank Herbert", "Science fiction"),
        Book("The left hand of Darkness", "Ursula le Guin", "Science fiction")
    ]

    organize_books(books)