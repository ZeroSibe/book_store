# class BookRepository():

#     def all():
#         # Selecting all records
#         # No arguments
#         # Executes the SQL query:
#         # SELECT id, title, author_name FROM books;

#         # Returns an array of Book objects.

#     def find(id):
#         # Gets a single record by its ID
#         # One argument: the id (number)
#         # Executes the SQL query:
#         # SELECT id, title, author_name FROM books WHERE id = $1;

#         # Returns a single Book object.

#         # Add more methods below for each operation you'd like to implement.

#     def create(book):
#     # Executes the SQL query:
#     # INSERT INTO books (title, author_name) VALUES (%s, %s), [book.title, book.author_name];
#     # Retuns None

#     # One argument: the book (book instance)


#     # def update(book)
#     # 

#     # def delete(book)
#     # 