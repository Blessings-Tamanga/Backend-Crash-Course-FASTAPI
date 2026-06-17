from fastapi import APIRouter, HTTPException
from app.schemas import Student
from app.databases import students

route = APIRouter()

@route.get("/students")
def get_students():
    return students

@route.get("/students/{student_id}")
def get_student(student_id : int):
    for student in students:
        if student["id"] == student_id:
            return student
    raise HTTPException(status_code = 404, detail="student not found")

@route.post("/students")
def add_student(student: Student):
    new_student = {
        "id" : len(students) + 1,
        "name" : student.name,
        "age" : student.age,
        "course" : student.course
    }

    students.append(new_student)
    return new_student

@route.put("/students/{student_id}")
def update_student(student_id : int, updated_student : Student):
    for student in students:
        if student["id"] == student_id:
            student["name"]  = updated_student.name
            student["age"] = updated_student.age
            student["course"] = updated_student.course
            return student
    raise HTTPException(status_code=404, detail="student not dound")

@route.delete("/students/{student_id}")
def delete_student(student_id : int):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return {"message": "student removed"}
        
    raise HTTPException(status_code=404 , detail= "student not found")