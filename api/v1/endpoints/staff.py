from fastapi import APIRouter
from api.services.staff_service import StaffService
from api.schema.staff_schema import *

router=APIRouter()
student_service=StaffService()


@router.post("/update_new_staff_details",description="Update student details")
async def update_new_staff_details(staff_data: StaffModel):
    update_student=await student_service.update_new_staff_details(staff_data)
    update_student['status_code']=200 if update_student['success']==True else 500
    return update_student

@router.post("/get_staff_list",description="Get student list")
async def get_staff_list(staff_search_request: StaffSearchRequest):
    staff_list=await student_service.get_staff_list(staff_search_request)
    staff_list['status_code']=200 if staff_list['success']==True else 500
    return staff_list

@router.delete("/delete_staff_details",description="Delete student details")
async def delete_staff_details(staff_id: str):
    delete_student=await student_service.delete_staff_details(staff_id)
    delete_student['status_code']=200 if delete_student['success']==True else 500
    return delete_student