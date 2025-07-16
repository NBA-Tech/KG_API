from pydantic import BaseModel
from typing import List, Optional, Literal


class StudentParentModel(BaseModel):
    father_name: Optional[str]=None
    mother_name: Optional[str]=None
    parent_contact_no: Optional[str]=None
    email: Optional[str]=None
    guardian_contact_no: Optional[str]=None


class StudentClassModel(BaseModel):
    class_name: Optional[str]=None
    section: Optional[str]=None
    roll_no: Optional[str]=None


class StudentModel(BaseModel):
    student_id: Optional[str]=None
    first_name: Optional[str]=None
    last_name: Optional[str]=None
    date_of_birth: Optional[str]=None
    student_class: StudentClassModel
    student_parent: StudentParentModel
    gender: Optional[Literal["male", "female","other"]] = None
    address: Optional[str]=None
    student_profile_photo: Optional[str]=None
    student_birth_certificate: Optional[str]=None
    student_created_on: Optional[str]=None
    student_status: Optional[bool]=True
    blood_group: Optional[str]=None
    religion: Optional[str]=None
    caste: Optional[str]=None
    other_notes: Optional[str]=None
    mother_tongue: Optional[str]=None


class StudentSearchRequest(BaseModel):
    filters: Optional[dict] = None
    page:Optional[int]=1
    page_size:Optional[int]=10
    required_fields: Optional[List[str]] = None
    search_query:Optional[str]=None
    get_all:Optional[bool]=False
