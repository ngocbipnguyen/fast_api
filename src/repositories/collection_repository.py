from sqlalchemy.orm import Session
from src.models.collection_model import CollectionModel

class CollectionRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_collection_by_id(self, collection_id: str):
        return self.db.query(CollectionModel).filter(CollectionModel.id == collection_id).first()

    def create_collection(self, collection_data: dict):
        new_collection = CollectionModel(**collection_data)
        self.db.add(new_collection)
        self.db.commit()
        self.db.refresh(new_collection)
        return new_collection
    
    def get_collections_by_user_id(self, user_id: str):
        return self.db.query(CollectionModel).filter(CollectionModel.user_id == user_id).all()
    
    def get_all_collections(self):
        return self.db.query(CollectionModel).all()
    