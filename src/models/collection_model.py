from sqlalchemy import Column, String, Boolean, Integer, BigInteger, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
Base = declarative_base()

class CollectionModel(Base):
    __tablename__ = "collections"

    id = Column(String, primary_key=True)  # Kotlin String
    title = Column(String, nullable=False)
    description = Column(String)
    is_private = Column(Boolean, default=False)
    media_count = Column(Integer, default=0)
    photos_count = Column(Integer, default=0)
    videos_count = Column(Integer, default=0)
    timestamps = Column(BigInteger)

    # FK to user
    user_id = Column(String, ForeignKey("user.id"))
    user = relationship("UserModel", back_populates="collections")

    # relationship: 1 collection -> N medias
    pixel = relationship("PixelsPhotoModel", back_populates="collection")
