from app.database import students

def create_student(student):
    new_student = {
        "id": len(students) + 1,
        "name": student.name,
        "class_name": student.class_name
    }
    students.append(new_student)
    return new_student