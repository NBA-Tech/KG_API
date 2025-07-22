from db.mongo_collections import MonogoCollections
import asyncio
from core.helpers import *
import re
from schema.setting_schema import *


class SettingService:
    def __init__(self):
        self.mongo_collections = MonogoCollections()

    async def update_setting_details(self, setting_data: SettingModel):
        try:
            setting_dict = setting_data.dict()

            if not setting_dict.get("setting_id"):
                setting_data.setting_id = generate_random_string(10)
                setting_dict["setting_id"] = setting_data.setting_id

            setting_id = setting_dict.pop("setting_id")

            await asyncio.to_thread(
                self.mongo_collections.SETTINGS_DB["WEB_SETTINGS"].update_one,
                {"setting_id": setting_id},
                {"$set": setting_dict},  # ✅ Proper dictionary usage
                upsert=True  # Optional: insert if not found
            )

            return {"success": True, "message": "Setting record updated successfully"}

        except Exception as e:
            return {"success": False, "message": str(e)}

