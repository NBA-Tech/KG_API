from db.mongo_collections import MonogoCollections
import asyncio
from core.helpers import *
import re
from schema.students_schema import *


class StudentService:
    def __init__(self):
        self.mongo_collections = MonogoCollections()

    
    async def update_new_student(self, student_data: StudentModel):
        try:
            # Generate ID and timestamp if new
            if not student_data.student_id:
                total_count = await self.mongo_collections.STUDENT_DB["STUDENTS_DETAILS"].count_documents({})
                student_data.student_id = generate_random_string(10,"student",total_count)
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
                    self.mongo_collections.STUDENT_DB["STUDENTS_DETAILS"].update_one,
                    {"student_id": student_data.student_id},
                    update_query,
                    upsert=True
                )

            return {"success": True, "message": "Student record created or updated successfully"}

        except Exception as e:
            return {"success": False, "message": str(e)}
        
    async def get_student_list(self, student_search_request: StudentSearchRequest):
        try:
            mongo_query = {}

            # Filters
            if isinstance(student_search_request.filters, dict) and student_search_request.filters:
                for key, value in student_search_request.filters.items():
                    if isinstance(value, list):
                        mongo_query[key] = {"$in": value}
                    else:
                        mongo_query[key] = value

            # Optional search query - can be extended
            if student_search_request.search_query:
                search_regex = {"$regex": re.escape(student_search_request.search_query), "$options": "i"}
                mongo_query["$or"] = [{"first_name": search_regex}, {"last_name": search_regex}]

            projection = {"_id": 0}

            # If get_all flag is set
            if student_search_request.get_all:
                student_cursor = self.mongo_collections.STUDENT_DB["STUDENTS_DETAILS"].find(mongo_query, projection)
                student_list = list(student_cursor)
                return {
                    "success": True,
                    "message": "All Students fetched successfully",
                    "students": student_list,
                    "page": 1,
                    "page_size": len(student_list),
                    "total_students": len(student_list)
                }

            # Pagination
            page = student_search_request.page or 1
            page_size = student_search_request.page_size or 10
            skip = (page - 1) * page_size

            cursor = (
                self.mongo_collections.STUDENT_DB["STUDENTS_DETAILS"]
                .find(mongo_query, projection)
                .skip(skip)
                .limit(page_size)
            )
            student_list = list(cursor)
            total_count = self.mongo_collections.STUDENT_DB["STUDENTS_DETAILS"].count_documents(mongo_query)

            return {
                "success": True,
                "message": "Students fetched successfully",
                "students": student_list,
                "page": page,
                "page_size": page_size,
                "total_students": total_count
            }

        except Exception as e:
            return {"success": False, "message": str(e)}


    async def delete_student_details(self,student_id):
        try:
            await asyncio.to_thread(
                self.mongo_collections.STUDENT_DB["STUDENTS_DETAILS"].delete_one,
                {"student_id": student_id}
            )
            return {"success": True, "message": "Student record deleted successfully"}
        except Exception as e:
            return {"success": False, "message": str(e)}
