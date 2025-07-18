from typing import List, Optional
from pydantic import BaseModel



class EventTimeModel(BaseModel):
    event_start_time: Optional[str] = None
    event_end_time: Optional[str] = None
    event_venue: Optional[str] = None
    event_target_audience: Optional[str] = None
    is_registration_required: Optional[bool] = True
    event_registration_deadline: Optional[str] = None
    event_max_participants: Optional[int] = None


class EventPosterModel(BaseModel):
    event_cover_photo: Optional[str] = None
    event_banner_photo: Optional[str] = None
    event_additional_media: Optional[str] = None



class EventModel(BaseModel):
    event_id: Optional[str] = None
    event_title: Optional[str] = None
    event_description: Optional[str] = None
    event_type: Optional[str] = None
    event_organizer: Optional[str] = None
    event_date: Optional[str] = None
    event_status: Optional[bool] = True
    event_created_on: Optional[str] = None
    event_time: EventTimeModel
    event_poster: EventPosterModel
    event_hightlights: Optional[str] = None


class EventSearchRequest(BaseModel):
    filters: Optional[dict] = None
    page:Optional[int]=1
    page_size:Optional[int]=10
    required_fields: Optional[List[str]] = None
    search_query:Optional[str]=None
    get_all:Optional[bool]=False
