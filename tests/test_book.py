from lib.book import Book
### test_book.py

#1
# Book constructs with an id, title and author name
def test_book_constructs():
    book = Book(1, 'Test title', 'Test name')
    assert book.id ==  1
    assert book.title ==  'Test title'
    assert book.author_name ==  'Test name'

#2
# Format book object to string 
def test_book_format():
    book = Book(1, 'Test title', 'Test name')
    assert str(book) == 'Book(1, Test title, Test name)'

#3 
# Two identical instances of Book are equal
def test_equality():
    book_1 = Book(1, 'Test title', 'Test name')
    book_2 = Book(1, 'Test title', 'Test name')
    assert book_1 == book_2
