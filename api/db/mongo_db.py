from pymongo import MongoClient
from api.core.config import config

MONGO_CLIENT=None


def connect_to_mongo():
    global MONGO_CLIENT

    if MONGO_CLIENT is None:
        MONGO_CLIENT = MongoClient(config.DATABASE_URI)
        print("Connected to MongoDB")

def get_mongo_client():
    global MONGO_CLIENT
    return MONGO_CLIENT


def close_mongo_connection():
    if MONGO_CLIENT is not None:
        MONGO_CLIENT.close()

