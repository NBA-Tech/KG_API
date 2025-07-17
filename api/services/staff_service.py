from db.mongo_collections import MonogoCollections
import asyncio
from core.helpers import *
import re
from schema.staff_schema import *



class StaffService:
    def __init__(self):
        self.mongo_collections = MonogoCollections()

    
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
                    self.mongo_collections.STAFF_DB["STAFF_DETAILS"].update_one,
                    {"staff_id": staff_data.staff_id},
                    update_query,
                    upsert=True
                )

            return {"success": True, "message": "Staff record created or updated successfully"}

        except Exception as e:
            return {"success": False, "message": str(e)}
        

    async def get_staff_list(self, staff_search_request: StaffSearchRequest):
        try:
            mongo_query = {}

            # Filters
            if isinstance(staff_search_request.filters, dict) and staff_search_request.filters:
                for key, value in staff_search_request.filters.items():
                    if isinstance(value, list):
                        mongo_query[key] = {"$in": value}
                    else:
                        mongo_query[key] = value

            # Optional search query - can be extended
            if staff_search_request.search_query:
                search_regex = {"$regex": re.escape(staff_search_request.search_query), "$options": "i"}
                mongo_query["$or"] = [{"staff_info.first_name": search_regex}, {"staff_info.last_name": search_regex}]

            projection = {"_id": 0}

            # If get_all flag is set
            if staff_search_request.get_all:
                staff_cursor = self.mongo_collections.STAFF_DB["STAFF_DETAILS"].find(mongo_query, projection)
                staff_list = list(staff_cursor)
                return {
                    "success": True,
                    "message": "All Staff fetched successfully",
                    "staffs": staff_list,
                    "page": 1,
                    "page_size": len(staff_list),
                    "total_staffs": len(staff_list)
                }

            # Pagination
            page = staff_search_request.page or 1
            page_size = staff_search_request.page_size or 10
            skip = (page - 1) * page_size

            cursor = (
                self.mongo_collections.STAFF_DB["STAFF_DETAILS"]
                .find(mongo_query, projection)
                .skip(skip)
                .limit(page_size)
            )
            staff_list = list(cursor)
            total_count = self.mongo_collections.STAFF_DB["STAFF_DETAILS"].count_documents(mongo_query)

            return {
                "success": True,
                "message": "Staff fetched successfully",
                "staffs": staff_list,
                "page": page,
                "page_size": page_size,
                "total_staffs": total_count
            }

        except Exception as e:
            return {"success": False, "message": str(e)}