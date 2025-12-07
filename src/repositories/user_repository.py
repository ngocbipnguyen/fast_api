from sqlalchemy.orm import Session
from src.models.user_model import UserModel,ProfileModel

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_id(self, user_id: str):
        return self.db.query(UserModel).filter(UserModel.id == user_id).first()

    def create_user(self, user_data: dict):
        new_user = UserModel(**user_data)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user
    

class ProfileRepository:
    def __init__(self, db: Session):
        self.db = db

    # Add profile-related database operations here
    def get_profile_by_user_id(self, user_id: str):
        return self.db.query(ProfileModel).filter(ProfileModel.user_id == user_id).first()
    def create_profile(self, profile_data: dict):
        new_profile = ProfileModel(**profile_data)
        self.db.add(new_profile)
        self.db.commit()
        self.db.refresh(new_profile)
        return new_profile
    
    