from fastapi import APIRouter, Depends,UploadFile, File,Form
from api.services.firebase_service import FirebaseStorageService


router=APIRouter()
firebase_storage_service=FirebaseStorageService()



@router.post("/upload_file", description="Upload file to Firebase Storage")
async def upload_file(
    file: UploadFile = File(...),
    image_path: str = Form(...)
):
    image_url=firebase_storage_service.upload_file_from_bytes(file.file.read(), image_path, file.content_type)
    if(image_url):
        return {"success": True, "message": "File uploaded successfully", "image_url": image_url}
    return {"success": False, "message": "File upload failed"}