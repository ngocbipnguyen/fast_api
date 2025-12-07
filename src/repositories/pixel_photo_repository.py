from sqlalchemy.orm import Session
from src.models.pixels_photo_model import PixelsPhotoModel
from src.models.photo_src_model import PhotoSrcModel

class PixelPhotoRepository:
    def __init__(self, db: Session):
        self.db = db

    
    def get_pixel_photo_by_id(self, photo_id: str):
        return self.db.query(PixelsPhotoModel).filter(PixelsPhotoModel.id == photo_id).first()
    
    def create_pixel_photo(self, photo_data: dict):
        new_photo = PixelsPhotoModel(**photo_data)
        self.db.add(new_photo)
        self.db.commit()
        self.db.refresh(new_photo)
        return new_photo
    
    def get_pixel_photos_by_user_id(self, user_id: str):
        return self.db.query(PixelsPhotoModel).filter(PixelsPhotoModel.user_id == user_id).all()
    
    def get_all_pixel_photos(self):
        return self.db.query(PixelsPhotoModel).all()
    
    def get_pixel_photos_by_collection_id(self, collection_id: str):
        return self.db.query(PixelsPhotoModel).filter(PixelsPhotoModel.collection_id == collection_id).all()
    
    

class PhotoSrcRepository:
    def __init__(self, db: Session):
        self.db = db

    # Add photo source-related database operations here 
    def get_photo_src_by_photo_id(self, photo_id: str):
        return self.db.query(PhotoSrcModel).filter(PhotoSrcModel.photo_id == photo_id).all()
    
    def create_photo_src(self, photo_src_data: dict):
        new_photo_src = PhotoSrcModel(**photo_src_data)
        self.db.add(new_photo_src)
        self.db.commit()
        self.db.refresh(new_photo_src)
        return new_photo_src
    
    def get_all_photo_srcs(self):
        return self.db.query(PhotoSrcModel).all()
    