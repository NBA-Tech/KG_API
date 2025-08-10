from fastapi import APIRouter
from api.services.student_service import StudentService
from api.schema.students_schema import *
router=APIRouter()
student_service=StudentService()


@router.post("/update_new_student",description="Update student details")
async def update_new_student(student_data: StudentModel):
    update_student=await student_service.update_new_student(student_data)
    update_student['status_code']=200 if update_student['success']==True else 500
    return update_student


@router.post("/get_student_list",description="Get student list")
async def get_student_list(student_search_request: StudentSearchRequest):
    student_list=await student_service.get_student_list(student_search_request)
    student_list['status_code']=200 if student_list['success']==True else 500
    return student_list

@router.delete("/delete_student_details",description="Delete student details")
async def delete_student_details(student_id: str):
    delete_student=await student_service.delete_student_details(student_id)
    delete_student['status_code']=200 if delete_student['success']==True else 500
    return delete_student