from app.database import borrow_records, books

def borrow_book(request):
    # 1. Find book
    book = None
    for b in books:
        if b["id"] == request.book_id:
            book = b
            break

    if not book:
        return {"error": "Book not found"}

    # 2. Check availability
    if book["status"] != "available":
        return {"error": "Book already borrowed"}

    # 3. Create borrow record
    borrow = {
        "id": len(borrow_records) + 1,
        "student_id": request.student_id,
        "book_id": request.book_id,
        "librarian_id": request.librarian_id,
        "status": "borrowed"
    }

    borrow_records.append(borrow)

    # 4. Update book status
    book["status"] = "borrowed"

    return borrow