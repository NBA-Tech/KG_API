from fastapi import APIRouter
from services.contact_service import ContactService
from schema.contact_schema import *



router=APIRouter()
contact_service=ContactService()


@router.post("/update_contact_request_details",description="Update contact request details")
async def update_contact_request_details(contact_data: ContactModel):
    update_contact=await contact_service.update_contact_request_details(contact_data)
    update_contact['status_code']=200 if update_contact['success']==True else 500
    return update_contact

@router.get("/get_contact_request_details",description="Get contact request details")
async def get_contact_request_details(contact_id: str):
    contact_details=await contact_service.get_contact_request_details(contact_id)
    contact_details['status_code']=200 if contact_details['success']==True else 500
    return contact_details