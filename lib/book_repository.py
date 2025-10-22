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

    def update(self,book_id, book_title):
        self._connection.execute(
            'UPDATE books SET title = %s WHERE id = %s',[book_title, book_id])
        return None

    def delete(self, book_id):
        self._connection.execute(
            'DELETE from books WHERE id = %s', [book_id])
        return None