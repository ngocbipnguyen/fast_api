from src.repositories.collection_repository import CollectionRepository
from sqlalchemy.orm import Session

class CollectionService:
    def __init__(self, db: Session):
        self.repository = CollectionRepository(db)

    def get_collection_by_id(self, collection_id: str):
        return self.repository.get_collection_by_id(collection_id)
    
    def create_collection(self, collection_data: dict):
        return self.repository.create_collection(collection_data)
    
    def get_collections_by_user_id(self, user_id: str):
        return self.repository.get_collections_by_user_id(user_id)
    
    def get_all_collections(self):
        return self.repository.get_all_collections()