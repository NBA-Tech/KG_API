from fastapi import APIRouter
from api.services.setting_service import SettingService
from api.schema.setting_schema import *


router=APIRouter()
setting_service=SettingService()

@router.post("/update_setting_details",description="Update setting details")
async def update_setting_details(setting_data: SettingModel):
    update_setting=await setting_service.update_setting_details(setting_data)
    update_setting['status_code']=200 if update_setting['success']==True else 500
    return update_setting

@router.get("/get_setting_details",description="Get setting details")
async def get_setting_details():
    setting_details=await setting_service.get_setting_details()
    setting_details['status_code']=200 if setting_details['success']==True else 500
    return setting_details