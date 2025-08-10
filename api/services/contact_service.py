from api.db.mongo_collections import MonogoCollections
import asyncio
from api.core.helpers import *
import re
from api.schema.contact_schema import *


class ContactService:
    def __init__(self):
        self.mongo_collections = MonogoCollections()

    async def update_contact_request_details(self, contact_data: ContactModel):
        try:
            if(not contact_data.contact_id):
                total_count = await self.mongo_collections.CONTACT_DB["APPOINTMENT_REQUESTS"].count_documents({})
                contact_data.contact_id = generate_random_string(6,"contact",total_count)
                contact_data.created_on = get_current_date_time()
            raw_data = contact_data.dict(exclude_none=True)
            update_data = {
                k: v for k, v in raw_data.items()
                if not (v == "" or v == [] or v == 0)
            }
            update_query = {}
            if update_data:
                update_query["$set"] = update_data
            if update_query:
                await asyncio.to_thread(
                    self.mongo_collections.CONTACT_DB["APPOINTMENT_REQUESTS"].update_one,
                    {"contact_id": contact_data.contact_id},
                    update_query,
                    upsert=True
                )
            return {"success": True, "message": "Contact record created or updated successfully"}
        except Exception as e:
            return {"success": False, "message": str(e)}
        
    async def get_contact_request_details(self, contact_id: Optional[str] = None):
        try:
            collection = self.mongo_collections.CONTACT_DB["APPOINTMENT_REQUESTS"]
            
            if contact_id:
                contact_details = await collection.find_one({"contact_id": contact_id}, {"_id": 0})
            else:
                cursor = collection.find({}, {"_id": 0})
                contact_details = cursor.to_list(length=None)

            return {
                "success": True,
                "message": "Contact record(s) fetched successfully",
                "contact": contact_details
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"Error fetching contact details: {str(e)}"
            }
        

    async def delete_contact_request_details(self, contact_id: str):
        try:
            await asyncio.to_thread(
                self.mongo_collections.CONTACT_DB["APPOINTMENT_REQUESTS"].delete_one,
                {"contact_id": contact_id}
            )
            return {"success": True, "message": "Contact record deleted successfully"}
        except Exception as e:
            return {"success": False, "message": str(e)}