from db.mongo_collections import MonogoCollections
import asyncio
from core.helpers import *
import re
from schema.event_schema import *



class EventService:
    def __init__(self):
        self.mongo_collections = MonogoCollections()

    async def update_event_details(self, event_data: EventModel):
        try:
            # Generate ID and timestamp if new
            if not event_data.event_id:
                total_count = await self.mongo_collections.EVENT_DB["EVENT_DETAILS"].count_documents({})
                event_data.event_id = generate_random_string(10,"event",total_count)
                event_data.event_created_on = get_current_date_time()

            # Convert to dict and remove empty/invalid fields
            raw_data = event_data.dict(exclude_none=True)
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
                    self.mongo_collections.EVENT_DB["EVENT_DETAILS"].update_one,
                    {"event_id": event_data.event_id},
                    update_query,
                    upsert=True
                )

            return {"success": True, "message": "Event record created or updated successfully"}

        except Exception as e:
            return {"success": False, "message": str(e)}
        
    async def get_event_list(self, event_search_request: EventSearchRequest):
        try:
            mongo_query = {}

            # Filters
            if isinstance(event_search_request.filters, dict) and event_search_request.filters:
                for key, value in event_search_request.filters.items():
                    if isinstance(value, list):
                        mongo_query[key] = {"$in": value}
                    else:
                        mongo_query[key] = value

            # Optional search query - can be extended
            if event_search_request.search_query:
                search_regex = {"$regex": re.escape(event_search_request.search_query), "$options": "i"}
                mongo_query["$or"] = [{"event_title": search_regex}]

            projection = {"_id": 0}

            # If get_all flag is set
            if event_search_request.get_all:
                event_cursor = self.mongo_collections.EVENT_DB["EVENT_DETAILS"].find(mongo_query, projection)
                event_list = list(event_cursor)
                return {
                    "success": True,
                    "message": "All Event fetched successfully",
                    "events": event_list,
                    "page": 1,
                    "page_size": len(event_list),
                    "total_events": len(event_list)
                }

            # Pagination
            page = event_search_request.page or 1
            page_size = event_search_request.page_size or 10
            skip = (page - 1) * page_size

            cursor = (
                self.mongo_collections.EVENT_DB["EVENT_DETAILS"]
                .find(mongo_query, projection)
                .skip(skip)
                .limit(page_size)
            )
            event_list = list(cursor)
            total_count = self.mongo_collections.EVENT_DB["EVENT_DETAILS"].count_documents(mongo_query)

            return {
                "success": True,
                "message": "Events fetched successfully",
                "events": event_list,
                "page": page,
                "page_size": page_size,
                "total_events": total_count
            }

        except Exception as e:
            return {"success": False, "message": str(e)}
        
    async def delete_event_details(self,event_id):
        try:
            await asyncio.to_thread(
                self.mongo_collections.EVENT_DB["EVENT_DETAILS"].delete_one,
                {"event_id": event_id}
            )
            return {"success": True, "message": "Event record deleted successfully"}
        except Exception as e:
            return {"success": False, "message": str(e)}