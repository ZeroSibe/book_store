# {{TABLE NAME}} Model and Repository Classes Design Recipe

_Copy this recipe template to design and implement Model and Repository classes for a database table._

## 1. Design and create the Table

If the table is already created in the database, you can skip this step.

Otherwise, [follow this recipe to design and create the SQL schema for your table](https://journey.makers.tech/pages/single-table-design-recipe-template).

*In this template, we'll use an example table `students`*

```
# EXAMPLE

Table: books

Columns:
id | title | author_name
```

## 2. Create Test SQL seeds 

Your tests will depend on data stored in PostgreSQL to run.

If seed data is provided (or you already created it), you can skip this step.

```sql
-- EXAMPLE
-- (file: seeds/book_store.sql)

-- Write your SQL seed here. 

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS books;
DROP SEQUENCE IF EXISTS books_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS books_id_seq;
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    author_name VARCHAR(255)
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO books (title, author_name) VALUES ('Nineteen Eighty-Four', 'George Orwell');
INSERT INTO books (title, author_name) VALUES ('Mrs Dalloway', 'Virginia Woolf');
INSERT INTO books (title, author_name) VALUES ('Emma', 'Jane Austen');
INSERT INTO books (title, author_name) VALUES ('Dracula', 'Bram Stoker');
INSERT INTO books (title, author_name) VALUES ('The Age of Innocence', 'Edith Wharton');
```

Run this SQL file on the database to truncate (empty) the table, and insert the seed data. Be mindful of the fact any existing records in the table will be deleted.

```bash
psql -h 127.0.0.1 book_store < book_store.sql
```

## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python
# EXAMPLE
# Table name: students

# Model class
# (in lib/book.py)
class Book


# Repository class
# (in lib/book_repository.py)
class BookRepository

```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# EXAMPLE
# Table name: books

# Model class
# (in lib/book.py)

class Book:
    def __init__(self):
        self.id = 0
        self.title = ""
        self.author_name = ""

        # Replace the attributes by your own columns.


# We can set the attributes to default empty values and set them later,
# here's an example:
#
# >>> student = Student()
# >>> student.name = "Will"
# >>> student.cohort_name = "September Devs"
# >>> student.name
# 'Will'
# >>> student.cohort_name
# 'September Devs'

```

## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python
# EXAMPLE
# Table name: books

# Repository class
# (in lib/book_repository.py)

class BookRepository():

    def all():
        # Selecting all records
        # No arguments
        # Executes the SQL query:
        # SELECT id, title, author_name FROM books;

        # Returns an array of Book objects.

    def find(id):
        # Gets a single record by its ID
        # One argument: the id (number)
        # Executes the SQL query:
        # 'SELECT * FROM books WHERE id = %s', [id]

        # Returns a single Book object.


    def create(book):
        # One argument: the book (book instance)
        # # Executes the SQL query:
        # INSERT INTO books (title, author_name) VALUES (%s, %s), [book.title, book.author_name];
        # Returns None

    def update(book_id, book_title)
        # Update book record
        # Two arguments: passing book_id, book title
        # Executes the SQL query:
        # UPDATE books SET title = %s WHERE id = %s,[book_title, book_id]
        # Returns None

    def delete(book_id)
        # Remove book record
        # One argument: passing book_id
        # Executes the SQL query:
        # DELETE from books WHERE id = %s, [book_id]
        # Returns None

```

## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python

### test_book.py

#1
# Book constructs with an id, title and author name

book = Book(1, 'Test title', 'Test name')
book.id # =>  1
book.title # =>  'Test title'
book.author_name # =>  'Test name'

#2
# Format book object to string 
book = Book(1, 'Test title', 'Test name')
str(book) #=> 'Book(1, Test title, Test name)'

#3 
# Two identical instances of Book are equal
book_1 = Book(1, 'Test title', 'Test name')
book_2 = Book(1, 'Test title', 'Test name')
book_1 == book_2 #=> True

### test_book_repository.py
# 1
# Get all books

repo = BookRepository()

books = repo.all()

len(books) # =>  5

books[0].id # =>  1
books[0].title # =>  'Nineteen Eighty-Four'
books[0].author_name # =>  'George Orwell'

books[1].id # =>  2
books[1].title # =>  'Mrs Dalloway'
books[1].author_name # =>  'Virginia Woolf'

# 2
# Get a single book

repo = BookRepository()

book = repo.find(1)

book[0].id # =>  1
book[0].title # =>  'Nineteen Eighty-Four'
book[0].author_name # =>  'George Orwell'

# 3
# Create new book record
repo = BookRepository()

book = repo.create(Book('Atomic Habits', 'James Clear'))
books = repo.all()
len(books) # =>  6
book[-1].id # =>  6
book[-1].title # =>  'Atomic Habits'
book[-1].author_name # =>  'James Clear'

# 4
# Update book record
repo = BookRepository()

book = repo.update(1, 'Animal Farm')
books = repo.find(1)
book.id # =>  1
book.title # =>  'Animal Farm'
book.author_name # =>  'George Orwell'

# 5
# Remove book record
repo = BookRepository()

book = repo.delete(5)
books = repo.all()
len(books) # =>  4
books[-1].id # =>  4
books[-1].title # =>  'Dracula'
books[-1].author_name # =>  'Bram Stoker'


```

Encode this example as a test.


## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._