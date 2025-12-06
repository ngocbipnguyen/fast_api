from sqlalchemy import BigInteger, Column, ForeignKey, Integer, String, Boolean, BigInteger
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class UserModel(Base):
    __tablename__ = "user"

    id = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    photo_url = Column(String, nullable=True)
    token = Column(String, unique=True, nullable=True)
    time_login = Column(BigInteger, nullable=True)
    follow = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    profile = relationship("ProfileModel", back_populates="user", uselist=False, cascade="all, delete")
    collections = relationship("CollectionModel", back_populates="user", cascade="all, delete")
    social = relationship("SocialModel", back_populates="user", cascade="all, delete")

class ProfileModel(Base):
    __tablename__ = "profile"

    id = Column(String, ForeignKey("user.id"), primary_key=True)
    totalView = Column(BigInteger, default=0)
    allTimeRank = Column(BigInteger, default=0)
    monthRank = Column(BigInteger, default=0)

    user = relationship("UserModel", back_populates="profile")