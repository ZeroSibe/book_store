from lib.book import Book

class BookRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM books')
        return [Book(row['id'], row['title'], row['author_name']) for row in rows ]

    def find(self, id):
        rows = self._connection.execute('SELECT * FROM books WHERE id = %s', [id])
        row = rows[0]
        return Book(row['id'], row['title'], row['author_name'])

    def create(self, book):
        self._connection.execute(
            'INSERT INTO books (title, author_name) VALUES (%s, %s)',
            [book.title, book.author_name])
        return None

    # def update(book)
    # 

    # def delete(book)
    # 