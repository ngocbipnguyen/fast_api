from sqlalchemy.orm import Session
from src.models.social_model import SocialModel

class SocialRepository:


    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(SocialModel).all()

    def create(self, social: SocialModel):
        self.db.add(social)
        self.db.commit()
        self.db.refresh(social)
        return social
    def get_by_user_id(self, user_id: str):
        return self.db.query(SocialModel).filter(SocialModel.user_id == user_id).all()
    
    
    
