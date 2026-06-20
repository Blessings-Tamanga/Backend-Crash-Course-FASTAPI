from fastapi import APIRouter
from app.schemas.student import Student
from app.services.student_service import create_student
from app.database import students

router = APIRouter()

@router.post("/students")
def add_student(student: Student):
    return create_student(student)


@router.get("/students")
def get_students():
    return students

@router.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    return {"detail": "Student not found"}

@router.delete("/students/{student_id}")
def delete_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return {"message": "Student deleted"}
    return {"detail": "Student not found"}