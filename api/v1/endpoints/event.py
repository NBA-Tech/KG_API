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


@router.post("/get_event_list",description="Get event list")
async def get_event_list(event_search_request: EventSearchRequest):
    event_list=await event_service.get_event_list(event_search_request)
    event_list['status_code']=200 if event_list['success']==True else 500
    return event_list

@router.delete("/delete_event_details",description="Delete event details")
async def delete_event_details(event_id: str):
    delete_event=await event_service.delete_event_details(event_id)
    delete_event['status_code']=200 if delete_event['success']==True else 500
    return delete_event