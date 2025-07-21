from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional, Literal


class GalleryModel(BaseModel):
    gallery_id: Optional[str] = None
    gallery_title: Optional[str] = None
    gallery_description: Optional[str] = None
    gallery_image_uri: Optional[str] = None
    gallery_created_on: Optional[datetime] = None