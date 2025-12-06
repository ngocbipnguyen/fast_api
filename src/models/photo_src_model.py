from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import declarative_base,relationship

Base = declarative_base()

class PhotoSrcModel(Base):
    __tablename__ = "photo_src"

    id = Column(Integer, ForeignKey("pixels_photo.id"), primary_key=True, index=True)
    original = Column(String, nullable=False)
    large = Column(String, nullable=False)
    medium = Column(String, nullable=False)
    small = Column(String, nullable=False)

    photo = relationship("PixelsPhotoModel", back_populates="src")