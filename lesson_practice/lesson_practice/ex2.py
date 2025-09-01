from book import Book

library = [Book('The Shawshank Redemption', 'Stephen King'),
           Book('Woe from Wit', 'Aleksandr Griboyédov'),
           Book('Pride and Prejudice', 'Jane Austen')
           ]

for book in library:
    print(f'Название книги: {book.get_name()}, автор: {book.get_autor()}')
