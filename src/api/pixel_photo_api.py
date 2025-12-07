from fastapi import APIRouter, Depends
from typing import List
from src.schemas.pixel_photo import PixelPhoto, PhotoSrc
from src.services.pixel_photo_service import PixelPhotoService, PhotoSrcService
from sqlalchemy.orm import Session
from src.db.session import get_db

photo_router = APIRouter()

@photo_router.get("/photos", response_model=List[PixelPhoto])
def get_all_photos():
    db: Session = Depends(get_db)
    service = PixelPhotoService(db)
    return service.get_all_pixel_photos()
@photo_router.post("/photos", response_model=PixelPhoto)
def create_photo(photo_data: dict, db: Session = Depends(get_db)):
    service = PixelPhotoService(db)
    return service.create_pixel_photo(photo_data)

@photo_router.get("/photos/{photo_id}", response_model=PixelPhoto)
def get_photo_by_id(photo_id: str, db: Session = Depends(get_db)):
    service = PixelPhotoService(db)
    return service.get_pixel_photo_by_id(photo_id)

@photo_router.get("/photos/user/{user_id}", response_model=List[PixelPhoto])
def get_photos_by_user_id(user_id: str, db: Session = Depends(get_db)):
    service = PixelPhotoService(db)
    return service.get_pixel_photos_by_user_id(user_id)

@photo_router.get("/photos/collection/{collection_id}", response_model=List[PixelPhoto])
def get_photos_by_collection_id(collection_id: str, db: Session = Depends(get_db)):
    service = PixelPhotoService(db)
    return service.get_pixel_photos_by_collection_id(collection_id)

@photo_router.get("/photo-srcs", response_model=List[PhotoSrc])
def get_all_photo_srcs(db: Session = Depends(get_db)):
    service = PhotoSrcService(db)
    return service.get_all_photo_srcs()

@photo_router.post("/photo-srcs", response_model=PhotoSrc)
def create_photo_src(photo_src_data: dict, db: Session = Depends(get_db)):
    service = PhotoSrcService(db)
    return service.create_photo_src(photo_src_data)
