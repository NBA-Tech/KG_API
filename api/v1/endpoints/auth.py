from fastapi import APIRouter, Query
from api.services.auth_service import AuthService
from api.schema.auth_schema import *



router=APIRouter()
auth_service=AuthService()


@router.post("/check_login",description="Check login")
async def check_login(login_data: LoginModel):
    check_login=await auth_service.check_login(login_data)
    check_login['status_code']=200 if check_login['success']==True else 500
    return check_login



