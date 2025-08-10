from api.db.mongo_collections import MonogoCollections
import asyncio
from api.core.helpers import *
import re
from api.schema.gallery_schema import *


class GalleryService:
    def __init__(self):
        self.mongo_collections = MonogoCollections()

    async def update_gallery_details(self, gallery_data: GalleryModel):
        try:
            # Generate ID and timestamp if new
            if not gallery_data.gallery_id:
                total_count = self.mongo_collections.EVENT_DB["GALLERY_DETAILS"].count_documents({})
                gallery_data.gallery_id = generate_random_string(10,"gallery",total_count)
                gallery_data.gallery_created_on = get_current_date_time()

            # Convert to dict and remove empty/invalid fields
            raw_data = gallery_data.dict(exclude_none=True)
            update_data = {
                k: v for k, v in raw_data.items()
                if not (v == "" or v == [] or v == 0 or v==None)
            }

            update_query = {}
            if update_data:
                update_query["$set"] = update_data

            # Only run update if there's something to update
            if update_query:
                await asyncio.to_thread(
                    self.mongo_collections.EVENT_DB["GALLERY_DETAILS"].update_one,
                    {"gallery_id": gallery_data.gallery_id},
                    update_query,
                    upsert=True
                )

            return {"success": True, "message": "Gallery record created or updated successfully"}

        except Exception as e:
            return {"success": False, "message": str(e)}
        
    async def get_gallery_details(self):
        try:
            gallery_cursor = self.mongo_collections.EVENT_DB["GALLERY_DETAILS"].find({}, {"_id": 0})
            gallery_list = list(gallery_cursor)
            return {"success": True, "message": "All gallery fetched successfully", "gallery": gallery_list}
        except Exception as e:
            return {"success": False, "message": str(e)}
        
    async def delete_gallery_details(self, gallery_id: str):
        try:
            await asyncio.to_thread(
                self.mongo_collections.EVENT_DB["GALLERY_DETAILS"].delete_one,
                {"gallery_id": gallery_id}
            )
            return {"success": True, "message": "Gallery record deleted successfully"}
        except Exception as e:
            return {"success": False, "message": str(e)}