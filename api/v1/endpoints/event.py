from fastapi import APIRouter
from services.event_service import EventService
from schema.event_schema import *


router=APIRouter()
event_service=EventService()


@router.post("/update_event_details",description="Update event details")
async def update_event_details(event_data: EventModel):
    update_event=await event_service.update_event_details(event_data)
    update_event['status_code']=200 if update_event['success']==True else 500
    return update_event