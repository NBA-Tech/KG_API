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
                event_data.event_id = generate_random_string(10)
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