from fastapi import APIRouter
from services.setting_service import SettingService
from schema.setting_schema import *


router=APIRouter()
setting_service=SettingService()

@router.post("/update_setting_details",description="Update setting details")
async def update_setting_details(setting_data: SettingModel):
    update_setting=await setting_service.update_setting_details(setting_data)
    update_setting['status_code']=200 if update_setting['success']==True else 500
    return update_setting