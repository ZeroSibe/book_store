from lib.book import Book
from lib.book_repository import BookRepository

### test_book_repository.py
# 1
# Get all books
def test_get_all_books(db_connection):
    db_connection.seed('seeds/book_store.sql')
    repo = BookRepository(db_connection)

    books = repo.all()
    assert len(books) ==  5

    assert books[0].id ==  1
    assert books[0].title ==  'Nineteen Eighty-Four'
    assert books[0].author_name ==  'George Orwell'

    assert books[1].id ==  2
    assert books[1].title ==  'Mrs Dalloway'
    assert books[1].author_name ==  'Virginia Woolf'

# 2
# Get a single book
def test_get_single_book(db_connection):
    db_connection.seed('seeds/book_store.sql')
    repo = BookRepository(db_connection)

    book = repo.find(1)

    assert book.id ==  1
    assert book.title ==  'Nineteen Eighty-Four'
    assert book.author_name ==  'George Orwell'

# 3
# Create new book record
def test_create_book(db_connection):
    db_connection.seed('seeds/book_store.sql')
    repo = BookRepository(db_connection)

    book = repo.create(Book(None, 'Atomic Habits', 'James Clear'))
    books = repo.all()

    assert len(books) ==  6
    assert books[-1].id ==  6
    assert books[-1].title ==  'Atomic Habits'
    assert books[-1].author_name ==  'James Clear'

# # 4
# # Update book record
# repo = BookRepository()

# book = repo.update(1, 'Animal Farm')
# books = repo.find(1)
# book.id # =>  1
# book.title # =>  'Animal Farm'
# book.author_name # =>  'George Orwell'

# # 5
# # Remove book record
# repo = BookRepository()

# book = repo.delete(5)
# books = repo.all()
# len(books) # =>  4
# book[-1].id # =>  4
# book[-1].title # =>  'Dracula'
# book[-1].author_name # =>  'Bram Stoker'