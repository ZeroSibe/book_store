from lib.database_connection import DatabaseConnection
from lib.book_repository import BookRepository
from lib.book import Book


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/book_store.sql")

# Retrieve all artists
book_repository = BookRepository(connection)
books = book_repository.all()

# List them out
for book in books:
    print(book)

# Find book
print(book_repository.find(2))

# Create new book
book_repository.create(Book(None, 'Atomic Habits', 'James Clear'))
books = book_repository.all()

# List them out
for book in books:
    print(book)

# Update book record
book_repository.update(1, 'Animal Farm')
print(book_repository.find(1))

# Remove book record
book_repository.delete(4)
print(book_repository.all())


