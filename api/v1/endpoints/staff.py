from fastapi import APIRouter
from services.staff_service import StaffService
from schema.staff_schema import *

router=APIRouter()
student_service=StaffService()


@router.post("/update_new_staff_details",description="Update student details")
async def update_new_staff_details(staff_data: StaffModel):
    update_student=await student_service.update_new_staff_details(staff_data)
    update_student['status_code']=200 if update_student['success']==True else 500
    return update_student
