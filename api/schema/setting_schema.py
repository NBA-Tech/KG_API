from typing import List, Literal, Optional, Union
from pydantic import BaseModel, Field
from datetime import datetime


# === Base type (abstract) ===
class BaseSettingModel(BaseModel):
    type: str
    setting_id: Optional[str] = None


# === Concrete setting types with discriminator ===
class HomeCarouselSettingModel(BaseSettingModel):
    type: Literal["home_carousel"]
    home_carousel_title: Optional[str] = None
    home_carousel_description: Optional[str] = None
    home_carousel_image_uri: Optional[str] = None
    home_carousel_created_on: Optional[datetime] = None


class StaffListSettingModel(BaseSettingModel):
    type: Literal["staff_info"]
    staff_ids: Optional[List[str]] = None


class ClassInfoSettingModel(BaseSettingModel):
    type: Literal["class_info"]
    class_ids: Optional[List[str]] = None

class EventInfoSettingModel(BaseSettingModel):
    type: Literal["event_info"]
    event_ids: Optional[List[str]] = None


class TestimonialSettingModel(BaseSettingModel):
    type: Literal["testimonial"]
    testimonial_person_name: Optional[str] = None
    testimonial_description: Optional[str] = None
    testimonial_image_uri: Optional[str] = None
    testimonial_created_on: Optional[datetime] = None


# === Discriminated Union Type (as the parent schema) ===
SettingModel = Union[
    HomeCarouselSettingModel,
    StaffListSettingModel,
    ClassInfoSettingModel,
    TestimonialSettingModel,
    EventInfoSettingModel
]
