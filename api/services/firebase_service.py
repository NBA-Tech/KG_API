# services/firebase_storage_service.py

from google.cloud import storage
from api.db.firebase_client import get_bucket
from typing import Optional
import mimetypes


class FirebaseStorageService:
    def __init__(self):
        self.bucket = get_bucket()  # Ensure this returns a storage.Bucket instance

    def upload_file_from_bytes(self, file_bytes: bytes, file_path: str, content_type: Optional[str] = None) -> str:
        blob = self.bucket.blob(file_path)
        blob.upload_from_string(file_bytes, content_type=content_type or mimetypes.guess_type(file_path)[0])
        blob.make_public()
        return blob.public_url

    def delete_file(self, file_path: str) -> bool:
        blob = self.bucket.blob(file_path)
        if blob.exists():
            blob.delete()
            return True
        return False

    def get_file_url(self, file_path: str) -> Optional[str]:
        blob = self.bucket.blob(file_path)
        if blob.exists():
            return blob.public_url
        return None

    def file_exists(self, file_path: str) -> bool:
        return self.bucket.blob(file_path).exists()