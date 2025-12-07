from fastapi import APIRouter, Depends
from typing import List
from src.schemas.collection import Collection
from sqlalchemy.orm import Session
from src.db.session import get_db
from src.services.collection_service import CollectionService

collection_router = APIRouter()

@collection_router.get("/collections", response_model=List[Collection])
def get_all_collections(db: Session = Depends(get_db)):
    service = CollectionService(db)
    return service.get_all_collections()

@collection_router.post("/collections", response_model=Collection)
def create_collection(collection_data: dict, db: Session = Depends(get_db)):
    service = CollectionService(db)
    return service.create_collection(collection_data)

@collection_router.get("/collections/user/{user_id}", response_model=List[Collection])
def get_collections_by_user_id(user_id: str, db: Session = Depends(get_db)):
    service = CollectionService(db)
    return service.get_collections_by_user_id(user_id)