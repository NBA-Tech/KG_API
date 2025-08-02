from db.mongo_collections import MonogoCollections
import asyncio
from core.helpers import *
import re
from schema.auth_schema import *


class AuthService:
    def __init__(self):
        self.mongo_collections = MonogoCollections()

    async def check_login(self, login_data: LoginModel):
        if(login_data.login_type=="admin"):
            if(login_data.email=="kgadmin@gmail.com" and login_data.password=="admin@123"):
                return {"success": True, "message": "Login successful","login_type":login_data.login_type}
            else:
                return {"success": False, "message": "Login failed","login_type":login_data.login_type}
            
        elif(login_data.login_type=="teacher"):
            mongo_query={
                     "staff_auth.email": login_data.email,
                     "staff_auth.password": login_data.password
                }
            staff_cursor = self.mongo_collections.STAFF_DB["STAFF_DETAILS"].find_one(mongo_query)
            if(staff_cursor):
                return {"success": True, "message": "Login successful","login_type":login_data.login_type}
            else:
                return {"success": False, "message": "Login failed","login_type":login_data.login_type}