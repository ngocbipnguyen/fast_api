
from sqlalchemy.orm import Session
from src.repositories.user_repository import UserRepository ,ProfileRepository


class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def get_user_by_id(self, user_id: str):
        return self.repository.get_user_by_id(user_id) 
    
    def create_user(self, user_data: dict):
        return self.repository.create_user(user_data)
    

class ProfileService:
    def __init__(self, db: Session):
        self.repository = ProfileRepository(db)

    # Add profile-related service methods here
    def get_profile_by_user_id(self, user_id: str):
        return self.repository.get_profile_by_user_id(user_id)
    
    def create_profile(self, profile_data: dict):
        return self.repository.create_profile(profile_data)
    