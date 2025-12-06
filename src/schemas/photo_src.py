from pydantic import BaseModel

class PhotoSrc(BaseModel):
    id: int
    original: str
    large: str
    medium: str
    small: str
