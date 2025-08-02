from typing import List, Literal, Optional
from pydantic import BaseModel
from datetime import datetime


class LoginModel(BaseModel):
    email: str
    password: str
    login_type: Literal["teacher", "admin"]