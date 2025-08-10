from fastapi import APIRouter
from api.services.gallery_service import GalleryService
from api.schema.gallery_schema import *



router=APIRouter()
gallery_service=GalleryService()

@router.post("/update_gallery_details",description="Update gallery details")
async def update_gallery_details(gallery_data: GalleryModel):
    update_gallery=await gallery_service.update_gallery_details(gallery_data)
    update_gallery['status_code']=200 if update_gallery['success']==True else 500
    return update_gallery

@router.get("/get_gallery_details",description="Get gallery details")
async def get_gallery_details():
    gallery_details=await gallery_service.get_gallery_details()
    gallery_details['status_code']=200 if gallery_details['success']==True else 500
    return gallery_details

@router.delete("/delete_gallery_details",description="Delete gallery details")
async def delete_gallery_details(gallery_id: str):
    delete_gallery=await gallery_service.delete_gallery_details(gallery_id)
    delete_gallery['status_code']=200 if delete_gallery['success']==True else 500
    return delete_gallery