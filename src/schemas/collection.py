from pydantic import BaseModel
from typing import List

from .pixel_photo import PixelPhoto


class Collection(BaseModel):
    id: str
    title: str
    description: str
    isPrivate: bool
    photos_count: int
    videos_count: int
    timestamps: int
    user_id: str

    pixels: List[PixelPhoto] = []

    class Config:
        orm_mode = True