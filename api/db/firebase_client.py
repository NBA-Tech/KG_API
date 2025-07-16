import firebase_admin
from firebase_admin import credentials, storage
from core.config import config


cred=None
bucket=None

def connect_to_firebase():
    global cred,bucket
    if(cred is not None and bucket is not None): return
    cred = credentials.Certificate(config.FIREBASE_CREDS)
    firebase_admin.initialize_app(cred, {'storageBucket': config.STORAGE_BUCKET_ID})
    bucket = storage.bucket()
    print(bucket)

def get_bucket():
    return bucket

connect_to_firebase()