from db.mongo_collections import MonogoCollections
import asyncio
from core.helpers import *
import re
from schema.staff_schema import *



class StaffService:
    def __init__(self):
        self.mongo_client = MonogoCollections()

    
    async def update_new_staff_details(self, staff_data: StaffModel):
        try:
            # Generate ID and timestamp if new
            if not staff_data.staff_id:
                staff_data.staff_id = generate_random_string(10)
                staff_data.student_created_on = get_current_date_time()

            # Convert to dict and remove empty/invalid fields
            raw_data = staff_data.dict(exclude_none=True)
            update_data = {
                k: v for k, v in raw_data.items()
                if not (v == "" or v == [] or v == 0)
            }

            update_query = {}
            if update_data:
                update_query["$set"] = update_data

            # Only run update if there's something to update
            if update_query:
                await asyncio.to_thread(
                    self.mongo_client.STAFF_DB["STAFF_DETAILS"].update_one,
                    {"staff_id": staff_data.staff_id},
                    update_query,
                    upsert=True
                )

            return {"success": True, "message": "Student record created or updated successfully"}

        except Exception as e:
            return {"success": False, "message": str(e)}