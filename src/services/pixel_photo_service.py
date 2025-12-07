from sqlalchemy.orm import Session
from src.repositories.pixel_photo_repository import PixelPhotoRepository, PhotoSrcRepository


class PixelPhotoService:
    def __init__(self, db: Session):
        self.repository = PixelPhotoRepository(db)

    def get_pixel_photo_by_id(self, photo_id: str):
        return self.repository.get_pixel_photo_by_id(photo_id)
    
    def create_pixel_photo(self, photo_data: dict):
        return self.repository.create_pixel_photo(photo_data)
    
    def get_pixel_photos_by_user_id(self, user_id: str):
        return self.repository.get_pixel_photos_by_user_id(user_id)
    
    def get_all_pixel_photos(self):
        return self.repository.get_all_pixel_photos()
    
    def get_pixel_photos_by_collection_id(self, collection_id: str):
        return self.repository.get_pixel_photos_by_collection_id(collection_id)
    
class PhotoSrcService:
    def __init__(self, db: Session):
        self.repository = PhotoSrcRepository(db)

    # Add photo source-related service methods here 
    def get_photo_src_by_photo_id(self, photo_id: str):
        return self.repository.get_photo_src_by_photo_id(photo_id)
    
    def create_photo_src(self, photo_src_data: dict):
        return self.repository.create_photo_src(photo_src_data)
    
    def get_all_photo_srcs(self):
        return self.repository.get_all_photo_srcs() 
