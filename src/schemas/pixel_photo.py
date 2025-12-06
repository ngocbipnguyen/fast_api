from pydantic import BaseModel


class PhotoSrc(BaseModel):
    id: int
    original: str
    large: str
    medium: str
    small: str

class PixelPhoto(BaseModel):
    id: int
    title: str
    description: str
    width: int
    height: int
    avgColor: str
    timestamps: int
    isFavorite: bool
    isMark: bool
    photo_src: PhotoSrc
    collection_id: str
    # user: User
    class Config:
        orm_mode = True
