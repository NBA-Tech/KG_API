from fastapi import APIRouter
from services.student_service import StudentService
from schema.students_schema import *
router=APIRouter()
student_service=StudentService()


@router.post("/update_new_student",description="Update student details")
async def update_new_student(student_data: StudentModel):
    update_student=await student_service.update_new_student(student_data)
    update_student['status_code']=200 if update_student['success']==True else 500
    return update_student
