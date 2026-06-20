from app.database import books

def create_book(book):
    new_book = {
        "id": len(books) + 1,
        "title" : book.title,
        "author" : book.author,
        "concept" : book.concept,
        "pages" : book.pages,
        "borrowing_cost" : book.cost,
        "status" : "available"
    }

    books.append(new_book)
    return new_book