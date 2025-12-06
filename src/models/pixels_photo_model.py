from sqlalchemy import Column, Integer, String, Boolean, BigInteger, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class PixelsPhotoModel(Base):
    __tablename__ = "pixels_photo"

    id = Column(BigInteger, primary_key=True, index=True)
    type = Column(String, nullable=False)
    photographerId = Column(BigInteger, nullable=False)
    photographer = Column(String, nullable=False)
    photographerUrl = Column(String, nullable=False)
    url = Column(String, nullable=False)
    width = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    avgColor = Column(String, nullable=False)
    timestamps = Column(BigInteger, nullable=False)
    isFavorite = Column(Boolean, default=False)
    isFollow = Column(Boolean, default=False)
    isMark = Column(Boolean, default=False)

    # FK to src
    photo_src = relationship("PhotoSrcModel", back_populates="photo")


    # back relation
    collection_id = Column(String, ForeignKey("collections.id"))
    collection = relationship("CollectionModel", back_populates="pixel")