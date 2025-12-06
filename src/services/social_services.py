from sqlalchemy.orm import Session
from src.repositories.social_repository import SocialRepository
from src.models.social_model import SocialModel

class SocialService:

    def __init__(self, db: Session):
        self.repository = SocialRepository(db)

    def get_all_socials(self):
        return self.repository.get_all()

    def create_social(self, social_data):
        social = SocialModel(**social_data)
        return self.repository.create(social)

    def get_socials_by_user_id(self, user_id: str):
        return self.repository.get_by_user_id(user_id)