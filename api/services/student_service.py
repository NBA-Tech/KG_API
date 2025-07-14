from db.mongo_collections import MonogoCollections
import asyncio
from core.helpers import *
import re
from schema.students_schema import *


class StudentService:
    def __init__(self):
        self.mongo_client = MonogoCollections()

    
    async def update_new_student(self, student_data: StudentModel):
        try:
            # Generate ID and timestamp if new
            if not student_data.student_id:
                student_data.student_id = generate_random_string(10)
                student_data.student_created_on = get_current_date_time()

            # Convert to dict and remove empty/invalid fields
            raw_data = student_data.dict(exclude_none=True)
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
                    self.mongo_client.STUDENT_DB["STUDENTS_DETAILS"].update_one,
                    {"student_id": student_data.student_id},
                    update_query,
                    upsert=True
                )

            return {"success": True, "message": "Student record created or updated successfully"}

        except Exception as e:
            return {"success": False, "message": str(e)}

