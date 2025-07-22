from typing import List, Literal, Optional
from pydantic import BaseModel
from datetime import datetime

class ContactModel(BaseModel):
    contact_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    child_name: Optional[str] = None
    child_age: Optional[str] = None
    message: Optional[str] = None
    created_on: Optional[datetime] = None
    appointment_expected_date: Optional[datetime] = None