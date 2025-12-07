from sqlalchemy import BigInteger, Column, Integer, String, Boolean, BigInteger,ForeignKey
from sqlalchemy.orm import declarative_base,relationship
Base = declarative_base()

class SocialModel(Base):
    __tablename__ = "social"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    icon_url = Column(String, nullable=False)
    link = Column(String, nullable=False)
    # FK
    user_id = Column(String, ForeignKey("user.id"))
    user = relationship("UserModel", back_populates="social")  


