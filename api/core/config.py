from dotenv import load_dotenv
import os


load_dotenv()


class Config:
    DATABASE_URI = os.getenv("DATABASE_URI")
    FIREBASE_CREDS = os.getenv("FIREBASE_CREDS_PATH")
    STORAGE_BUCKET_ID = os.getenv("STORAGE_BUCKET_ID")

config =Config()