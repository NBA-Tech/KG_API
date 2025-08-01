from pydantic import BaseModel
from typing import List, Optional, Literal


class StaffInfoModel(BaseModel):
    first_name: Optional[str]=None
    last_name: Optional[str]=None
    gender: Optional[Literal["male", "female"]] = None
    primary_contact_number: Optional[str]=None
    email_address: Optional[str]=None
    blood_group: Optional[str]=None
    date_of_birth: Optional[str]=None
    marital_status: Optional[str]=None
    status: Optional[bool]=True
    staff_profile_photo: Optional[str]=None


class StaffExperienceInfo(BaseModel):
    handling_classes: Optional[List[str]]=None
    subject: Optional[List[str]]=None
    date_of_joining: Optional[str]=None
    qualification: Optional[str]=None
    language_known: Optional[List[str]]=None
    work_experience: Optional[str]=None
    notes: Optional[str]=None


class StaffParentInfo(BaseModel):
    fathers_name: Optional[str]=None
    mothers_name: Optional[str]=None
    parent_contact_no: Optional[str]=None
    address: Optional[str]=None
    permanent_address: Optional[str]=None

class StaffBankInfo(BaseModel):
    account_name: Optional[str]=None
    account_number: Optional[str]=None
    bank_name: Optional[str]=None
    ifsc_code: Optional[str]=None
    branch_name: Optional[str]=None
    salary: Optional[str] = None


class StaffKYCInfo(BaseModel):
    resume_file: Optional[str]=None
    joining_letter: Optional[str]=None
    id_number: Optional[str]=None

class StaffAuthModel(BaseModel):
    email: Optional[str]=None
    password: Optional[str]=None
    
class StaffModel(BaseModel):
    staff_id: Optional[str]=None
    student_created_on: Optional[str]=None
    staff_info: StaffInfoModel
    staff_experience_info: StaffExperienceInfo
    staff_parent_info: StaffParentInfo
    staff_bank_info: StaffBankInfo
    staff_kyc_info: StaffKYCInfo
    staff_auth: StaffAuthModel


class StaffSearchRequest(BaseModel):
    filters: Optional[dict] = None
    page:Optional[int]=1
    page_size:Optional[int]=10
    required_fields: Optional[List[str]] = None
    search_query:Optional[str]=None
    get_all:Optional[bool]=False

