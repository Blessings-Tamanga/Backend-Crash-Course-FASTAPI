from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Student(BaseModel):
    name : str
    email : str


students = [] #sample database

#routes/endpoints work hand in hand with the HTTP Methods (Post,get,put,delete)
@app.get("/")
def get_info():
    return {"message":"API is working"}

#student management system
#read students
@app.get("/students")
def get_students():
    return students

@app.post("/students")
def create_student(student : Student):
    student_id = len(students) + 1
    new_student = {
        "student_id" : student_id,
        "name" : student.name,
        "email" : student.email
        }
    
    students.append(new_student)
    return students

@app.put("/students/{student_id}")
def update_student(student_id : int, updated_student: Student):
    for student in students:
        if student_id == student["student_id"]:
            student["name"] = updated_student.name
            student["email"] = updated_student.email
            return {"message": "student updated", "student": student}
        
    