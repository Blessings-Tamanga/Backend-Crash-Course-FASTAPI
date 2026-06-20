from fastapi import APIRouter,HttpException
from app.database import librarians
from app.schemas import Librarian, UpdateLibrarian
from app.services import librarian_service

router = APIRouter()

@router.post("/librarians")
def add_librarian(librarian: Librarian):
    new_librarian = {
        "id": len(librarians) + 1,
        "name": librarian.name,
        "shift": librarian.shift
    }
    librarians.append(new_librarian)
    return new_librarian


@router.delete("/librarians/{librarian_id}")
def delete_librarian(librarian_id: int):
    for librarian in librarians:
        if librarian["id"] == librarian_id:
            librarians.remove(librarian)
            return {"message": "Librarian deleted"}

    raise HTTPException(status_code=404, detail="Librarian not found")


@router.put("/librarians/{librarian_id}")
def update_librarian(librarian_id: int, update: UpdateLibrarian):
    for librarian in librarians:
        if librarian["id"] == librarian_id:
            librarian["name"] = update.name
            librarian["shift"] = update.shift
            return librarian

    raise HTTPException(status_code=404, detail="Librarian not found")

@router.get("/librarians")
def get_librarians():
    return librarians


@router.get("/librarians/{librarian_id}")
def get_librarian(librarian_id: int):
    for librarian in librarians:
        if librarian["id"] == librarian_id:
            return librarian

    raise HTTPException(status_code=404, detail="Librarian not found")