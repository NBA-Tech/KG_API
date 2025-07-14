from pydantic import BaseModel
from typing import Optional, Literal


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
    name: Optional[str]=None
    student_class: StudentClassModel
    student_parent: StudentParentModel
    address: Optional[str]=None
    student_profile_photo: Optional[str]=None
    student_birth_certificate: Optional[str]=None
    student_created_on: Optional[str]=None