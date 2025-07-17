from db.mongo_db import get_mongo_client,connect_to_mongo

class MonogoCollections:
    def __init__(self):
        connect_to_mongo()
        self.mongo_client = get_mongo_client()
        self.STUDENT_DB = self.mongo_client["STUDENT_DB"]
        self.STAFF_DB = self.mongo_client["STAFF_DB"]
        self.EVENT_DB = self.mongo_client["EVENT_DB"]